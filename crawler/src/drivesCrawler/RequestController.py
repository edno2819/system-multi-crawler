from abc import ABC, abstractmethod
from src.utils.folder import format_folder_name
from src.utils.report import Report
from datetime import datetime
import traceback
import logging
import time
import os


class RequestController(ABC):
    CURRENT_URL = ""

    def __init__(self, config, request, storage, site_id):
        self.request = request
        self.storage = storage
        self.folder_path = self.getPathFile()
        self.log = logging.getLogger(self.__class__.__name__)
        self.report = Report(site_id)
        self.config = config

        if True:
            self.storage.createFolder(self.folder_path)

    def getPathFile(self):
        current_date = datetime.now()
        path = os.path.join(
            f"{self.__class__.__name__}", current_date.strftime("%d-%m-%Y")
        )
        return path

    def createFolderProduct(self, name: str) -> str:
        path = os.path.join(self.folder_path, format_folder_name(name))
        self.storage.createFolder(path)
        return path

    def saveXML(self, response, folder_path):
        self.storage.save(folder_path, f"{time.time()}.xml", response.content)

    def saveJson(self, response, folder_path):
        self.storage.save(folder_path, f"{time.time()}.json", response.content)

    def saveHTML(self, response, folder_path):
        self.storage.save(folder_path, f"{time.time()}.html", response.content)

    @abstractmethod
    def run(self):
        pass

    def getReport(self) -> str:
        return self.report.to_json()

    def getError(self, e, url) -> str:
        error_message = str(e)
        error_traceback = traceback.format_exc()
        self.report.add_error(url, error_message, error_traceback)
