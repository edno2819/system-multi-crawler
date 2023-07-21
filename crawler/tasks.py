"""
Módulo para gerenciar tarefas
"""
import os
import logging
import traceback
import pprint
from celery import Celery
from dotenv import load_dotenv

from src.drivesCrawler.RequestController import RequestController
from src.database.main import DatabaseManager
from src.utils import loadModules
from src.utils import config
from src.utils import discordAlert

load_dotenv()

config.setup_logging()
LOG = logging.getLogger("tasks")

CELERY_APP = Celery(broker=os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0"))

DATABASE = DatabaseManager()


@CELERY_APP.task
def run_site(site: str):
    """
    Run the crawler for a specific site.

    Args:
        site: The name of the site to crawl.

    Returns:
        The results of the crawl.
    """
    try:
        class_brand: RequestController = loadModules.load_class_brand(site)
        config_brand = loadModules.load_config_brand(site)

        site_item = DATABASE.get_site_by_name(site)

        if not class_brand or not config_brand or not site_item:
            return "Module not found"

        instance = class_brand(DATABASE, config_brand, site_item.id)
        instance.run()
        result = instance.getReport()

        # using result
        LOG.info(result)
        DATABASE.save_crawler(result)
        result["errors"] = len(result["errors"])
        result_formated = pprint.pformat(result, indent=4, width=1, sort_dicts=False)
        discordAlert.send_msg(f"Resultado do Crawler: \n{result_formated}")
        DATABASE.db_manager.close()

        return result
    except Exception as exc:
        error_message = str(exc)
        error_traceback = traceback.format_exc()

        LOG.error(
            "Menssagem de erro: %s\nTraceback: %s",
            error_message,
            error_traceback,
        )
        return error_message