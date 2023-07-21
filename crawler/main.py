from dotenv import load_dotenv
from src.utils import config
from tasks import run_site
import logging
import yaml


load_dotenv()
log = logging.getLogger("main")


def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    for site in config["sites"]:
        ##run_site.delay(site)
        run_site(site)


if __name__ == "__main__":
    config.setup_logging()
    log.debug("Busca Iniciada!")
    main()
    input()
