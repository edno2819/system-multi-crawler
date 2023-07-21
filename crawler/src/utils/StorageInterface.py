"""
Module to manage storage files
"""

import os
from pathlib import Path
from libcloud.storage.providers import get_driver
from libcloud.storage.types import Provider


class StorageInterface:
    """
    Class to manage storage interface
    """
    BUCKET = "./data/bucket"

    def __init__(self, aws_id, key):
        """
        Initialize the StorageInterface
        """
        self.local = bool(os.getenv("STORAGE_LOCAL", "True"))
        if not self.local:
            cls = get_driver(Provider.S3)
            self.driver = cls(aws_id, key)
        else:
            self.local_path = os.path.join(os.getcwd(), self.BUCKET)
            Path(self.local_path).mkdir(parents=True, exist_ok=True)

    def create_folder(self, folder_path):
        """
        Method to create folder
        """
        Path(os.path.join(self.local_path, folder_path)).mkdir(parents=True, exist_ok=True)

    def save(self, path, object_name, file):
        """
        Method to save file
        """
        if self.local:
            with open(os.path.join(self.local_path, path, object_name), "wb") as file_instance:
                file_instance.write(file)
        else:
            self.driver.upload_object(
                file, self.driver.get_container(self.BUCKET), 
                object_name
            )
