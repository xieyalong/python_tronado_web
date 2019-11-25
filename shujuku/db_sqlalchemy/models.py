
#说明：所有模型


#创建表字段信息
from sqlalchemy import Column,Integer,String,DateTime,Float,Text,Index
#获取数据库连接
from shujuku.db_sqlalchemy import conn

from datetime import datetime

#创建所有表，用的也很少，基本都是对模型的增伤改查
def create_db():
    conn.Base.metadata.create_all(bind=conn.engine)

#删除所有模型映射表,基本上用不到
def delete_db():
    conn.Base.metadata.drop_all(bind=conn.engine)

# 字段的监听
def  test():
    print('---------test-----------------')

#数据库表模型
class Student(conn.Base):
    #映射数据库表名
    __tablename__='student'
    # 主键，自增
    id=Column(Integer,primary_key=True,autoincrement=True)
    #唯一,不能为null，作为索引列
    # s_name=Column(String(20),unique=True,nullable=False,index=True)
    s_name = Column(String(20),  nullable=False,)
    #默认18,表字段是“age”
    s_age=Column(type_=Integer,default=18,name='age')
    #显示为2019-11-25-15.35.41 +0800
    create_time = Column(DateTime, default=datetime.now)
    #显示为2019-11-25-15.35.41 +0800，
    # onupdate=datetime.now：修改时不用管此字段，它会自动更新
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    #String(20)==varchar(20)必须带长度
    #Text：不用带长度
    title=Column(Text)
    #comment='内容'：注解
    # doc='内容' 写不写无所谓
    #onupdate=test()该字段的监听，表的创建，添加数据,修改数据都会走此函数
    content = Column(type_=Text, doc='内容', comment='内容',onupdate=test())
    # color=Column(type_=Text,doc='颜色', comment='颜色')

    #设置索引等
    # __table_args__ = (Index('index(zone,status)', 'resource_zone', 'resource_status'), {'comment': '压测资源表'})  # 添加索引和表注释
    # #返回字符串
    def __repr__(self):
        return "<User(naem=%s, fullname=%s, password=%s)>" % (self.s_name, self.title, self.s_age)
        pass

    # # 返回字符串
    # def __set__(self, instance, value):
    #     pass

class xylUser(conn.Base):
    # 映射数据库表名
    __tablename__ = 'xyl_user'
    # 主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False,name='xyl_name' )







