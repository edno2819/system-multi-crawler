import json
from datetime import datetime


class Report:
    def __init__(self, site_id):
        self.data = {
            "site_id": site_id,
            "started_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "finished_at": "",
            "categories": 0,
            "products": 0,
            "errors": [],
        }

    def add_categories(self):
        self.data["categories"] += 1
        
    def add_products(self):
        self.data["products"] += 1

    def add_error(self, url:str, msg:str, backtrace:str):
        erro = {
            "url": url,
            "message": msg,
            "backtrace": backtrace,
        }
        self.data["errors"].append(erro)

    def to_json(self):
        self.data["finished_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return json.dumps(self.data)
