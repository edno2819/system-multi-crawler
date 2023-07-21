"""
Class for serving inheritance and implementing common methods 
for scripts to crawl websites using http requests.
"""

import traceback
import logging
import time
import os
from datetime import datetime
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

from src.utils.requests import RequestInterface
from src.utils.StorageInterface import StorageInterface
from src.utils.folder import format_folder_name
from src.utils.report import Report


class RequestController(ABC):
    """
    Class inheritance to implement scritps crawler
    """

    CURRENT_URL = ""

    def __init__(self, database, config, site_id):
        self.database = database
        self.site_id = site_id
        self.request = RequestInterface()
        self.storage = StorageInterface(
            os.getenv("STORAGE_ID", ""), os.getenv("STORAGE_KEY", "")
        )
        self.folder_path = self.get_path_file()
        self.log = logging.getLogger(self.__class__.__name__)
        self.report = Report(site_id)
        self.config = config

        self.storage.create_folder(self.folder_path)

    def get_path_file(self):
        current_date = datetime.now()
        path = os.path.join(
            f"{self.__class__.__name__}", current_date.strftime("%d-%m-%Y")
        )
        return path

    def create_folder_product(self, name: str) -> str:
        path = os.path.join(self.folder_path, format_folder_name(name))
        self.storage.create_folder(path)
        return path

    def save_xml(self, response, folder_path):
        self.storage.save(folder_path, f"{time.time()}.xml", response)

    def save_json(self, response, folder_path):
        self.storage.save(folder_path, f"{time.time()}.json", response)

    def save_html(self, response, folder_path):
        self.storage.save(folder_path, f"{time.time()}.html", response)

    def save_image(self, url, folder_path):
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

    def get_report(self) -> str:
        return self.report.getReport()

    def get_error(self, error, url) -> str:
        error_message = str(error)
        error_traceback = traceback.format_exc()
        self.report.add_error(url, error_message, error_traceback)

    def str_to_html_soup(self, html: str):
        return BeautifulSoup(html, "html.parser")

    def remove_header_from_html(self, html: BeautifulSoup):
        head_tag = html.find("head")
        if head_tag:
            head_tag.extract()
        return str(html)
