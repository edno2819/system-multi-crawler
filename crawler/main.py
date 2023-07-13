from src.utils.requests import RequestInterface
from src.utils.StorageInterface import StorageInterface
from src.drivesCrawler.RequestController import RequestController
from dotenv import load_dotenv
from pathlib import Path
import traceback
import logging
import os
import yaml
import importlib

load_dotenv()


log = logging.getLogger("main")


def load_config_brand(site) -> dict | None:
    try:
        with open(f"./src/brands/{site.lower()}/config.yaml") as f:
            return yaml.safe_load(f)
    except Exception as e:
        log.error(f"Erro ao carregar arquivo de configuração de {site}:\n {e}")
        return None


def load_class_brand(site) -> RequestController | None:
    try:
        module = importlib.import_module(f"src.brands.{site.lower()}.main")
        ClassBrand = getattr(module, site.capitalize())
        return ClassBrand
    except ModuleNotFoundError:
        log.error(f"No module found for site: {site}")
        return None


def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    request = RequestInterface()
    storage = StorageInterface(
        os.getenv("STORAGE_ID", ""), os.getenv("STORAGE_KEY", "")
    )

    for site in config["sites"]:
        ClassBrand: RequestController = load_class_brand(site)
        config_brand = load_config_brand(site)
        if not ClassBrand or not config_brand:
            break

        instance = ClassBrand(config_brand, request, storage, "DASG54")
        try:
            instance.run()
            log.info(instance.getReport())
        except Exception as e:
            error_message = str(e)
            error_traceback = traceback.format_exc()

            log.error(
                "Menssagem de erro: \n",
                error_message,
                "\nTRaceback teste: \n",
                error_traceback,
            )


if __name__ == "__main__":
    log_path = os.getenv("LOGS_PATH", "./logs")
    Path(log_path).mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Cria um manipulador de log que grava no arquivo
    file_handler = logging.FileHandler(log_path + "/log.log")
    file_handler.setLevel(logging.DEBUG)
    # Cria um manipulador de log que escreve no terminal
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    # Cria um formatador e adiciona ao manipulador
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    # Adiciona o manipulador ao logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.debug(f"Busca Iniciada!")
    main()
    logger.debug(f"Busca Finalizada!")
