
# 说明：连接数据库，并创建会话

#连接数据库
#安装 pip install sqlalchemy
#安装 pip install pymysql


#建立连接
from sqlalchemy import create_engine
# 模型与数据库表关联
from sqlalchemy.ext.declarative import  declarative_base
# 创建会话绑定数据库连接
from sqlalchemy.orm import sessionmaker

#连接数据库
db_url='mysql+pymysql://root:@127.0.0.1:3306/xyl_test'
#建立连接
engine=create_engine(db_url,
                     encoding='utf-8',
                     echo=True,
                     max_overflow=5,#允许在增加5个，一共是10个
                     pool_size=5,#连接池大小
                     pool_timeout=30,#池中没有连接等待的时间,否则报错
                     pool_recycle=-1#多久对线程池中的线程进行一次连接的回收，-1不回收，始终用原来那个
                     )

# 模型与数据库表关联
Base=declarative_base()

#会话绑定数据库连接 引入from sqlalchemy.orm import sessionmaker
dbSession=sessionmaker(bind=engine)
#增删改查操作数据
session=dbSession()
















