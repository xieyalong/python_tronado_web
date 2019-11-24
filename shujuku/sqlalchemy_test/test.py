
import sqlalchemy
from sqlalchemy import Integer, String, Float, Boolean, DateTime, Text, INTEGER, MetaData
from sqlalchemy.testing.schema import Column
print(sqlalchemy.__version__)

from  shujuku.sqlalchemy_test import test02

class Article(test02.Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)

test02.Base.metadata.create_all()

