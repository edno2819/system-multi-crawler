from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSON
import datetime

Base = declarative_base()

class Site(Base):
    __tablename__ = 'site'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    url = Column(String(255), nullable=False)

    def __repr__(self):
        return self.name


class Crawler(Base):
    __tablename__ = 'crawler'
    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey('site.id'), nullable=False)
    started_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    finished_at = Column(DateTime, nullable=False)
    categories = Column(Integer, default=0, nullable=False)
    products = Column(Integer, default=0, nullable=False)
    errors = Column(JSON, nullable=True)
    
    site = relationship("Site")

    def __repr__(self):
        return f'{self.site_id} - {self.started_at}'
