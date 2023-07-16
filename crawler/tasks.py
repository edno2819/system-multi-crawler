from src.drivesCrawler.RequestController import RequestController
from src.database.main import DatabaseManager
from src.utils import loadModules
from src.utils import config
from src.utils import discordAlert

from dotenv import load_dotenv
from celery import Celery
import traceback
import logging
import pprint
import os


load_dotenv()

config.setup_logging()
log = logging.getLogger("tasks")

celery_app = Celery(broker=os.getenv("CELERY_BROKER_URL", f"redis://redis:6379/0"))

databse = DatabaseManager()


@celery_app.task
def runSite(site: str):
    try:
        ClassBrand: RequestController = loadModules.load_class_brand(site)
        config_brand = loadModules.load_config_brand(site)

        site_item = databse.getSiteByName(site)

        if not ClassBrand or not config_brand or not site_item:
            return "Module not found"

        instance = ClassBrand(config_brand, site_item.id)
        instance.run()
        result = instance.getReport()

        # using result
        log.info(result)
        databse.saveCrawler(result)
        result["errors"] = len(result["errors"])
        result_formated = pprint.pformat(result, indent=4, width=1, sort_dicts=False)
        discordAlert.sendMsg(f"Resultado do Crawler: \n{result_formated}")

        return result

    except Exception as e:
        error_message = str(e)
        error_traceback = traceback.format_exc()

        log.error(
            "Menssagem de erro: \n",
            error_message,
            "\nTRaceback teste: \n",
            error_traceback,
        )
        return error_message


runSite("Arezzo")
