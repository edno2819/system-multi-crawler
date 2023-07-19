from src.drivesCrawler.RequestController import RequestController
from src.database.main import DatabaseManager
from src.database.models import *
from datetime import datetime
import json


class Arezzo(RequestController):
    CATEGORYS = [
        "SAPATOS",
        "BOLSAS",
    ]
    BASE_URL = "https://www.arezzo.com.br"

    def __init__(self, database: DatabaseManager, config: dict, site_id: str) -> None:
        super().__init__(database, config, site_id)
        self.size = 30
        self.max_itens = 600 * self.size

    def getUrl(self, category: str, page: int):
        base_api = "/arezzocoocc/v2/arezzo/products"
        url = f"/search?category={category}&currentPage={page}&pageSize={self.size}&fields=FULL&storeFinder=false"
        return self.BASE_URL + base_api + url

    def run(self):
        self.log.debug(f"Init crawler in {self.__class__.__name__}")

        for category in self.CATEGORYS:
            self.category = self.database.create_category_if_not_exists(
                category.lower()
            )
            self.report.add_categories()

            for page in range(0, self.max_itens):
                url = self.getUrl(category, page)
                res = self.request.send_request(url)
                self.saveJson(res.content, self.folder_path)
                data = res.json()
                
                if data["products"]==[]:
                    break

                for product in data["products"]:
                    self.log.info(f'Crawler product {product.get("name")}')
                    url_product = product.get("url")
                    self.current_url = self.BASE_URL + url_product

                    try:
                        self.current_path_product = self.createFolderProduct(
                            product.get("name")
                        )
                        self.getProducts(self.current_url, self.current_path_product)
                        self.report.add_products()
                    except Exception as e:
                        self.getError(e, url)

    def getProducts(self, url: str, path_product: str):
        res = self.request.send_request(url)
        if res.status_code == 200:
            if (
                "Content-Type" in res.headers
                and "text/html" in res.headers["Content-Type"]
            ):
                self.crawler_date = datetime.now()
                self.saveHTML(res.content, path_product)
                html_soup = self.strToHtmlSoup(res.content)
                self.getInfosByHtml(html_soup)
                return

        self.log.info(f"Response in {url} not found!")

    def getInfosProduct(self, html):
        script_tag = html.find("script", id="schema-tags")
        json_data = json.loads(script_tag.string)
        return json_data

    def getInfosByHtml(self, html):
        data = self.getInfosProduct(html)
        self.createItensFromJson(data)

    def createItensFromJson(self, data):
        product = self.saveProduct(data)
        self.setImage(data, product.id)
        self.setPrice(data, product.id)
        self.setSize(data, product.id)
        self.database.session.commit()

    def saveProduct(self, data):
        name = data.get("name")
        site_id = self.site_id
        sku = data.get("sku")
        category_id = self.category.id
        color = data.get("color")
        description = data.get("description", "")
        uri = self.current_url
        crawler_date = self.crawler_date

        product = self.database.create_product(
            name=name,
            site_id=site_id,
            sku=sku,
            category_id=category_id,
            uri=uri,
            crawler_date=crawler_date,
            description=description,
            color=color,
        )

        return product

    def setAttribute(self, data, product_id):
        attributes = data.get("attributes")
        if attributes:
            for attribute_data in attributes:
                attribute_name = attribute_data.get("name")
                score = attribute_data.get("score")

                attribute = (
                    self.database.session.query(Attribute)
                    .filter_by(name=attribute_name)
                    .first()
                )
                if not attribute:
                    attribute = Attribute(name=attribute_name)
                    self.database.session.add(attribute)

                product_attribute = ProductAttributes(
                    attribute_id=attribute.id, product_id=product_id, score=score
                )
                self.database.session.add(product_attribute)

    def setImage(self, data, product_id):
        image = data.get("image")
        if image:
            self.saveImage(image, self.current_path_product)
            picture_metadata = PictureMetadata(product_id=product_id, picture_url=image)
            self.database.session.add(picture_metadata)

    def setPrice(self, data, product_id):
        offers = data.get("offers")
        if offers:
            offer = offers[0]
            price = offer.get("price")
            promotional_price = 0  # offer.get("discountPrice").get("value")
            crawled_at = self.crawler_date

            product_price = ProductPrice(
                product_id=product_id,
                price=price,
                promotional_price=promotional_price,
                crawled_at=crawled_at,
            )
            self.database.session.add(product_price)

    def setSize(self, data, product_id):
        sizes = data.get("offers")
        if sizes:
            for size_data in sizes:
                size = size_data.get("sku").split("-")[1]
                if size_data.get("availability").find("Out") == -1:
                    stock = 0
                else:
                    stock = 10
                crawled_at = self.crawler_date
                product_size = ProductSizes(
                    product_id=product_id, size=size, stock=stock, crawled_at=crawled_at
                )
                self.database.session.add(product_size)
