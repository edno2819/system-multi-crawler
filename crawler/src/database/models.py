from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Site(Base):
    __tablename__ = "site"
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    url = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name


class Crawler(Base):
    __tablename__ = "crawler"
    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey("site.id"), nullable=False)
    started_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    finished_at = Column(DateTime, nullable=False)
    categories = Column(Integer, default=0, nullable=False)
    products = Column(Integer, default=0, nullable=False)
    errors = Column(JSON, nullable=True)

    site = relationship("Site")

    def __repr__(self):
        return f"{self.site_id} - {self.started_at}"


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)

    def __str__(self):
        return self.name


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    site_id = Column(Integer, ForeignKey("site.id"), nullable=False)
    sku = Column(String(512))
    category_id = Column(Integer, ForeignKey("categories.id"))
    color = Column(String(255))
    description = Column(String)
    uri = Column(String(255))
    crawler_date = Column(Date)
    metadata_product = Column(JSON, name="metadata")

    category = relationship("Category")

    def __str__(self):
        return self.name


class SubCategory(Base):
    __tablename__ = "sub_categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category = relationship("Category")

    def __str__(self):
        return f"{self.category_id} - {self.name}"


class ProductSizes(Base):
    __tablename__ = "products_sizes"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    size = Column(String(64))
    stock = Column(Integer)
    crawled_at = Column(Date)

    product = relationship("Product")

    def __str__(self):
        return f"{self.product_id} - {self.size} - {self.stock} - {self.crawled_at}"


class ProductPrice(Base):
    __tablename__ = "products_price"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    price = Column(Float)
    promotional_price = Column(Float)
    crawled_at = Column(Date)

    product = relationship("Product")

    def __str__(self):
        return str(self.product_id)


class Attribute(Base):
    __tablename__ = "attribute"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __str__(self):
        return self.name


class ProductAttributes(Base):
    __tablename__ = "products_attributes"

    id = Column(Integer, primary_key=True)
    attribute_id = Column(Integer, ForeignKey("attribute.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    score = Column(Float)

    attribute = relationship("Attribute")
    product = relationship("Product")

    def __str__(self):
        return str(self.attribute_id)


class PictureMetadata(Base):
    __tablename__ = "pictures_metadata"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    picture_url = Column(String(512))
    metadata_picture = Column(JSON, name="metadata")

    product = relationship("Product")

    def __str__(self):
        return str(self.product_id)
