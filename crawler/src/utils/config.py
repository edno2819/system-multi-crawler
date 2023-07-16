import logging
import datetime
import os
from pathlib import Path


def setup_logging():
    class LibsFilter(logging.Filter):
        def filter(self, record):
            if record.name == "root":
                return False
            return True if record.name.find(".") == -1 else False

    # format logging
    date = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%s")
    log_path = os.getenv("LOGS_PATH", "./logs")
    Path(log_path).mkdir(parents=True, exist_ok=True)

    log_filename = os.path.join(log_path, f"Crawler-{date}.log")
    log_level = logging.DEBUG

    logging.basicConfig(
        filename=log_filename,
        filemode="w",
        level=log_level,
        format="[%(asctime)s] [%(name)s] %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
    )
    libs_filter = LibsFilter()

    # Configura o console para exibir os logs com nível igual ou superior ao definido
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.addFilter(libs_filter)
    console_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] [%(name)s] %(levelname)s - %(message)s",
            datefmt="%H:%M:%S",
        )
    )
    # Adicionar filtro no logging
    
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        handler.addFilter(libs_filter)
    root_logger.addHandler(console_handler)
