

#导入模型,连接
from db_sqlalchemy import models,conn
from db_sqlalchemy.models import Cate,Resource
from db_sqlalchemy.conn import  session
#where语法
from sqlalchemy import or_,and_,text
from sqlalchemy.sql import func
from utils import strUtil
#创建表字段信息
from sqlalchemy import Column,Integer,String,DateTime, Text
#获取数据库连接
from  db_sqlalchemy.conn import  Base
from  db_sqlalchemy import  conn

from datetime import datetime
import  其他.用户信息.user_xlsx as ux


class omo_military_user(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    age=Column(Integer)
    user_name=Column(Text)
    name=Column(Text)
    #角色
    type=Column(Integer)
    parent_id=Column(Text)
    height=Column(Integer)
    weight=Column(Integer)
    birthday=Column(Text)

def add(age,user_name,name,type,parent_id,height,weight,birthday):
    u = omo_military_user()
    u.age=age
    u.user_name=user_name
    u.name=name
    u.type=type
    u.parent_id=parent_id
    u.height=height
    u.weight=weight
    u.birthday=birthday

    # 添加数据,如果有此数据就修改，没有此数据就添加
    conn.session.add(u)
    # 提交数据
    conn.session.commit()


if __name__ == '__main__':
    add(1,'1','1',1,'1',1,1)
    # ux.mian()