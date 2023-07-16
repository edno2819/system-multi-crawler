from src.drivesCrawler.RequestController import RequestController


class Arezzo(RequestController):
    CATEGORYS = ["BOLSAS", "SAPATOS"]
    BASE_URL = "https://www.arezzo.com.br"

    def __init__(self, config, site_id) -> None:
        super().__init__(config, site_id)
        self.size = 3
        self.max_itens = 2 * self.size

    def getUrl(self, category, page):
        base_api = "/arezzocoocc/v2/arezzo/products"
        url = f"/search?category={category}&currentPage={page}&pageSize={self.size}&fields=FULL&storeFinder=false"
        return self.BASE_URL + base_api + url

    def run(self):
        self.log.debug(f"Init crawler in {self.__class__.__name__}")

        for category in self.CATEGORYS:
            self.report.add_categories()
            for page in range(0, self.max_itens):
                url = self.getUrl(category, page)
                res = self.request.send_request(url)

                self.saveJson(res, self.folder_path)
                data = res.json()
                for product in data["products"]:
                    self.log.info(f'Crawler product {product.get("name")}')
                    url_product = product.get("url")
                    url = self.BASE_URL + url_product
                    try:
                        path_product = self.createFolderProduct(product.get("name"))
                        self.getProducts(url, path_product)
                        self.report.add_products()
                    except Exception as e:
                        self.getError(e, url)

    def getProducts(self, url: str, path_product: str):
        res = self.request.send_request(url)
        self.saveHTML(res, path_product)
