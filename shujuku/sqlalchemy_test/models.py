
#数据库连接,导入类型包
#DateTime:日期格式类型
from sqlalchemy import Integer, String, Float, Boolean, DateTime, Text, INTEGER
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.testing.schema import Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# pip install mysql-connector-python
#'mysql+mysqlconnector://root:@127.0.0.1:3306/xyl_test',
from  mysql import connector

engine=create_engine('mysql+mysqlconnector://root:@127.0.0.1:3306/xyl_test',
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
Session = sessionmaker(engine)
session = Session()



class User(Base):
    __tablename__ = 'xyluser'  #表格名字
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    title = Column(String(50))

    # 自己封装查询方法
    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_id(cls,id):
        return session.query(cls).filter_by(id=id).all()

    @classmethod
    def get_username(cls,username):
        return session.query(cls).filter_by(username=username).all()

    @property
    def locked(self):
        return self._locked

    def __repr__(self):
        return "<User(id='%s',username='%s',password='%s',creatime='%s',_locked='%s')>"%(
            self.id,
            self.username,
            self.password,
            self.creatime,
            self._locked
        )
if __name__=='__main__':
    # 验证是否成功可以在尾端进行如下操作：
    # print('base=',dir(Base))
    # print('session=',dir(session))
    # Base.metadata.create_all()

    # 验证
    # add_user()
    # delete_user()
    # update_user()
    # query_user()
    print('=========')
    print(User.get_id(1))  # 对上页封装的查询进行验证















