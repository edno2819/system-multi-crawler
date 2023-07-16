from libcloud.storage.providers import get_driver
from libcloud.storage.types import Provider
from pathlib import Path
import os


class StorageInterface:
    BUCKET = "./data/bucket"

    def __init__(self, id, key):
        self.local = bool(os.getenv("STORAGE_LOCAL", "True"))
        if not self.local:
            cls = get_driver(Provider.S3)
            self.driver = cls(id, key)
        else:
            self.local_path = os.path.join(os.getcwd(), self.BUCKET)
            Path(self.local_path).mkdir(parents=True, exist_ok=True)

    def createFolder(self, folder_path):
        Path(os.path.join(self.local_path, folder_path)).mkdir(parents=True, exist_ok=True)

    def save(self, path, object_name, file):
        if self.local:
            with open(os.path.join(self.local_path, path, object_name), "wb") as f:
                f.write(file)
        else:
            self.driver.upload_object(
                file, self.driver.get_container(self.BUCKET), 
                object_name
            )
