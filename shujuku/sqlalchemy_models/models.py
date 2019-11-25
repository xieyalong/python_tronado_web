
#说明：模型


#创建表字段信息
from sqlalchemy import Column,Integer,String
#获取数据库连接
from shujuku.sqlalchemy_models import conn


#创建所有表，用的也很少，基本都是对模型的增伤改查
def create_db():
    conn.Base.metadata.create_all(bind=conn.engine)

#删除所有模型映射表,基本上用不到
def delete_db():
    conn.Base.metadata.drop_all(bind=conn.engine)



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










