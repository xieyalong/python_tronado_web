
#说明：模型


#创建表字段信息
from sqlalchemy import Column,Integer,String
#获取数据库连接
from shujuku.sqlalchemy_models import conn


#创建表
def create_db():
    conn.Base.metadata.create_all(bind=conn.engine)


#数据库表模型
class Student(conn.Base):
    __tablename__='student'
    # 主键，自增
    id=Column(Integer,primary_key=True,autoincrement=True)
    #唯一,不能为null，
    s_name=Column(String(20),unique=True,nullable=False)
    #默认18
    s_age=Column(Integer,default=18)
    #默认18
    title=Column(String,default='title')










