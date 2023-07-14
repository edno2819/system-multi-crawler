from src.utils.requests import RequestInterface
from src.utils.StorageInterface import StorageInterface
from src.drivesCrawler.RequestController import RequestController
from src.utils import loadModules
from src.database.main import DatabaseManager
from src.database.models import Crawler

from dotenv import load_dotenv
from src.utils import config
from celery import Celery
import traceback
import logging
import os
import json

import datetime

load_dotenv()
celery_app = Celery(broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"))

log = logging.getLogger("tasks")


# database
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
db_manager = DatabaseManager(db_url)

db_manager.init_db()

# Obtém uma sessão de banco de dados
session = db_manager.db_session
new_crawler = Crawler(
    site_id=1,
    started_at=datetime.datetime.now(),
    finished_at=datetime.datetime.now(),
    categories=0,
    products=0,
    errors=[]
)

db_manager.db_session.add(new_crawler)
db_manager.commit()
db_manager.close()













@celery_app.task
def runSite(site: str):
    config.setup_logging()
    
    request = RequestInterface()
    storage = StorageInterface(
        os.getenv("STORAGE_ID", ""), os.getenv("STORAGE_KEY", "")
    )

    ClassBrand: RequestController = loadModules.load_class_brand(site)
    config_brand = loadModules.load_config_brand(site)

    if not ClassBrand or not config_brand:
        return "Module not found"

    instance = ClassBrand(config_brand, request, storage, "DASG54")

    try:
        instance.run()
        result = instance.getReport()
        log.info(result)
        result_dict = json.loads(result)
        result_dict["errors"] = len(result_dict["errors"])
        return result_dict
    except Exception as e:
        error_message = str(e)
        error_traceback = traceback.format_exc()

        log.error(
            "Menssagem de erro: \n",
            error_message,
            "\nTRaceback teste: \n",
            error_traceback,
        )
        return "Failure"
