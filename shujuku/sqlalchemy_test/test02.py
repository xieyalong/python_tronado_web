from sqlalchemy import Integer, String, Float, Boolean, DateTime, Text, INTEGER, MetaData
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.testing.schema import Column
from sqlalchemy import create_engine,ForeignKey


engine=create_engine('mysql+pymysql://root:@127.0.0.1:3306/xyl_test',
                     encoding='utf-8',
                     echo=True,
                     max_overflow=5,#允许在增加5个，一共是10个
                     pool_size=5,#连接池大小
                     pool_timeout=30,#池中没有连接等待的时间,否则报错
                     pool_recycle=-1#多久对线程池中的线程进行一次连接的回收，-1不回收，始终用原来那个
                     )

conn = engine.connect()
print('conn=',conn)
result = conn.execute("select 1")
print('======',result.fetchone())

Base = declarative_base(engine)





# class Article(Base):
#     __tablename__ = "article"
#     id = Column(Integer,primary_key=True,autoincrement=True)
#     title = Column(String(50),nullable=False)
#     uid = Column(Integer, ForeignKey("user.id"))




if __name__ == '__main__':
    Base.metadata.create_all()
