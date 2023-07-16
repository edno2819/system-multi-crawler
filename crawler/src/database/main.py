from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from src.database.models import Crawler, Site
import logging
import os


class SqlAlchemyInterface:
    def __init__(self, db_url):
        self.log = logging.getLogger(self.__class__.__name__)
        self.engine = create_engine(db_url)
        self.session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=self.engine))
        self.Base = declarative_base()

    def init_db(self):
        self.Base.metadata.create_all(bind=self.engine)
    
    def addItem(self, instanceTable):
        self.session.add(instanceTable)
    
    def cleanSession(self):
        ''' Limpa tudo que está na sessão'''
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
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')
        db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        self.db_manager = SqlAlchemyInterface(db_url)


    def getSiteByName(self, name):
        result = self.db_manager.session.query(Site).filter_by(name=name).first()
        return result
    
    def saveCrawler(self, crawler: dict):
        new_crawler = Crawler(
            site_id=crawler["site_id"],
            started_at=crawler["started_at"],
            finished_at=crawler["finished_at"],
            categories=crawler["categories"],
            products=crawler["products"],
            errors=crawler["errors"]
        )
        self.db_manager.addItem(new_crawler)
        self.db_manager.commit()
