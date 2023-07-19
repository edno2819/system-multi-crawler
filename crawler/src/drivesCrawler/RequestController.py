from src.utils.requests import RequestInterface
from src.utils.StorageInterface import StorageInterface
from src.utils.folder import format_folder_name
from src.utils.report import Report
from abc import ABC, abstractmethod
from datetime import datetime
from bs4 import BeautifulSoup
import traceback
import logging
import time
import os
import re


class RequestController(ABC):
    CURRENT_URL = ""

    def __init__(self, database, config, site_id):
        self.database = database
        self.site_id = site_id
        self.request = RequestInterface()
        self.storage = StorageInterface(
            os.getenv("STORAGE_ID", ""), os.getenv("STORAGE_KEY", "")
        )
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
        self.storage.save(folder_path, f"{time.time()}.xml", response)

    def saveJson(self, response, folder_path):
        self.storage.save(folder_path, f"{time.time()}.json", response)

    def saveHTML(self, response, folder_path):
        self.storage.save(folder_path, f"{time.time()}.html", response)

    def saveImage(self, url, folder_path):
        res = self.request.send_request(url)
        if res.status_code == 200:
            type_image = res.headers.get("Content-Type").split("/")
            if type_image[0] == "image":
                self.storage.save(
                    folder_path, f"{time.time()}.{type_image[1]}", res.content
                )

    @abstractmethod
    def run(self):
        pass

    def getReport(self) -> str:
        return self.report.getReport()

    def getError(self, e, url) -> str:
        error_message = str(e)
        error_traceback = traceback.format_exc()
        self.report.add_error(url, error_message, error_traceback)

    def strToHtmlSoup(self, html: str):
        return BeautifulSoup(html, "html.parser")

    def removeHeaderFromHtml(self, html: BeautifulSoup):
        head_tag = html.find("head")
        if head_tag:
            head_tag.extract()
        return str(html)
