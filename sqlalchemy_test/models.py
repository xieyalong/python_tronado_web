
#数据库连接,导入类型包
#DateTime:日期格式类型
from sqlalchemy import Integer, String, Float, Boolean, DateTime, Text, INTEGER
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.testing.schema import Column
from sqlalchemy import create_engine


print('=====')

#基类
Base=declarative_base()
class XylOrder(Base):
    #映射数据表名
    __tablename__ = 'xyl_order'
    # id= Column(Integer,primary_key=True,foreign_key_ddl=1)
    # String(200):长度200
    # nullable：是否可以为null,如果可以为nul就不用写
    #unique = True 是否唯一
    # name=Column('order_name',String(200),nullable=False)
    title = Column(String)
    # age=Column(Integer)
    # price = Column(Float)
    # update_time=Column(DateTime,nullable=False)
    # True=删除
    # is_delete=Column(Boolean,nullable=False)



print('-----------')
#连接数据库
# 'mysql://user:pwd@127.0.0.1:3306/omo_military'
# mysql+pymysql：连接mysql，用pymysql驱动
# root:用户名
# pwd：密码，密码可以为null 写成'mysql://root:@127.0.0.1:3306/omo_military'
# @localhost：主机地址 本地@127.0.0.1
# omo_military：数据库


# 创建数据库引擎，数据库的类名、账号、密码、登录方式、连接的数据库、数据库编码、是否显示回写
#
engine=create_engine('mysql+pymysql://root:@127.0.0.1:3306/xyl_test?charset=utf-8',
                     # encoding='utf-8',
                     # echo=True,
                     max_overflow=5,#允许在增加5个，一共是10个
                     pool_size=5,#连接池大小
                     pool_timeout=30,#池中没有连接等待的时间,否则报错
                     pool_recycle=-1#多久对线程池中的线程进行一次连接的回收，-1不回收，始终用原来那个
                     )

#创建继承Base的所有子类表
Base.metadata.create_all(engine)
#删除所有
# Base.metadata.drop_all(engine)




















