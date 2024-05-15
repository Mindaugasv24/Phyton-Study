import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

from db_project_sqla.constants import URL

engine = create_engine(URL)
Base = declarative_base()

class Project(Base):
    """representing class name and metods"""
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    price = Column("price", Float)
    created_date = Column("created_date", DateTime, default=datetime.datetime.utcnow)
    def __init__(self, name, price):
        """representing """
        self.name = name
        self.price = price
    def __repr__(self):
        """representing """
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"

Base.metadata.create_all(engine)
