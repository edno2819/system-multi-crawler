from dotenv import load_dotenv
from src.utils import config
from tasks import runSite
import logging
import yaml


load_dotenv()
log = logging.getLogger("main")


def main(alert=False):
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    for site in config["sites"]:
        ##runSite.delay(site)
        runSite(site)


if __name__ == "__main__":
    config.setup_logging()
    log.debug(f"Busca Iniciada!")
    main()
    input()
