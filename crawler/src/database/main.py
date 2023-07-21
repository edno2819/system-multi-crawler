from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from src.database import models
import logging
import os


class SqlAlchemyInterface:
    def __init__(self, db_url):
        self.log = logging.getLogger(self.__class__.__name__)
        self.engine = create_engine(db_url)
        self.session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        self.Base = declarative_base()

    def init_db(self):
        self.Base.metadata.create_all(bind=self.engine)

    def add_item(self, instanceTable):
        self.session.add(instanceTable)

    def clean_session(self):
        """Limpa tudo que está na sessão"""
        self.session.flush()

    def commit(self):
        try:
            # Persiste tudo que esta na sessão
            self.session.commit()
        except:
            self.session.rollback()
            raise

    def close(self):
        self.session.close()


class DatabaseManager:
    def __init__(self):
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        self.db_manager = SqlAlchemyInterface(db_url)
        self.session = self.db_manager.session

    def get_site_by_name(self, name):
        result = self.db_manager.session.query(models.Site).filter_by(name=name).first()
        return result

    def create_category_if_not_exists(self, name):
        category = self.session.query(models.Category).filter_by(name=name).first()
        if not category:
            category = models.Category(name=name)
            self.session.add(category)
            self.session.commit()
        return category

    def create_subcategory_if_not_exists(self, name, category_id):
        subcategory = (
            self.session.query(models.SubCategory)
            .filter_by(name=name, category_id=category_id)
            .first()
        )
        if not subcategory:
            subcategory = models.SubCategory(name=name, category_id=category_id)
            self.session.add(subcategory)
            self.session.commit()
        return subcategory

    def create_product(
        self,
        name,
        site_id,
        sku,
        category_id,
        uri,
        crawler_date,
        description="",
        color=None,
        metadata=None,
    ):
        product = models.Product(
            name=name,
            site_id=site_id,
            sku=sku,
            category_id=category_id,
            color=color,
            description=description,
            uri=uri,
            crawler_date=crawler_date,
            metadata=metadata,
        )
        self.session.add(product)
        self.session.commit()
        return product

    def save_crawler(self, crawler: dict):
        new_crawler = models.Crawler(
            site_id=crawler["site_id"],
            started_at=crawler["started_at"],
            finished_at=crawler["finished_at"],
            categories=crawler["categories"],
            products=crawler["products"],
            errors=crawler["errors"],
        )
        self.db_manager.add_item(new_crawler)
        self.db_manager.commit()
