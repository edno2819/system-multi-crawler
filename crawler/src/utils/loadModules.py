from src.drivesCrawler.RequestController import RequestController
import importlib
import logging
import yaml


log = logging.getLogger("LoadModules")


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

