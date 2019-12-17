
#说明：所有模型


#创建表字段信息
from sqlalchemy import Column, Integer, String, DateTime, Text, Float
#获取数据库连接
from  db_sqlalchemy.conn import  Base
from  db_sqlalchemy import  conn

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

class Cate(conn.Base):
    # 映射数据库表名
    __tablename__ = 'omo_pe_cate'
    # 主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    cate_name = Column(Text)
    parent_id=Column(Integer)
    img_url=Column(Text)
    type=Column(Integer)
    state=Column(Integer)


class Resource(Base):
    # 映射数据库表名
    __tablename__ = 'omo_resource'
    # 主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    resource_name = Column(String(200))
    cate_id=Column(Integer)
    content=Column(Text)
    type = Column(Integer)

class omo_military_user(Base):
    __tablename__ = 'omo_military_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # age=Column(Integer)
    user_name=Column(Text)
    name=Column(Text)
    #角色
    type=Column(Integer)
    parent_id=Column(Text)
    height=Column(Float)
    weight=Column(Float)
    birthday=Column(Integer)
    pwd=Column(Text)









# {
# "select * from omo_pe_cate LIMIT 1": [
# 	{
# 		"id" : 1,
# 		"type" : 1,
# 		"cate_name" : "颈部",
# 		"img_url" : "https:\/\/img00.yuanxinkangfu.com\/file\/resource\/20191\/1547024518714.png",
# 		"active_img_url" : "",
# 		"large_img_url" : "",
# 		"show_h5_page" : 0,
# 		"show_human_pic" : 0,
# 		"cate_sort" : 0,
# 		"parent_id" : 0,
# 		"state" : 0,
# 		"show_score" : 0,
# 		"score_operator_type" : null,
# 		"score_init" : null,
# 		"score_desc" : null,
# 		"cate_type" : 1,
# 		"desc" : "",
# 		"first_question" : 316,
# 		"created" : 1525343421,
# 		"updated" : 1536667654
# 	}
# ]}



# {
# "select * from omo_resource LIMIT  1": [
# 	{
# 		"id" : 1,
# 		"cate_id" : 1,
# 		"type" : 1,
# 		"resource_name" : "颈椎侧方稳定性训练",
# 		"duration" : 35,
# 		"state" : 0,
# 		"code" : "ZW-XL-42",
# 		"url" : "https:\/\/img00.yuanxinkangfu.com\/avthumb2\/file\/resource\/201811\/1541386938511.mp4",
# 		"url1" : null,
# 		"arr_url" : null,
# 		"content" : "[{\"url\":\"https:\/\/img00.yuanxinkangfu.com\/file\/resource\/20189\/1536746229387.jpeg\",\"des\":\"定位不清\"},{\"url\":\"http:\/\/img00.sun-hc.com\/file\/resource\/20186\/1529574210070.jpeg\",\"des\":\"注意事项：在治疗过程中，应及时询问用户的适应程度，如出现过烫，可再垫层毛巾，注意防止烫伤。\"}]",
# 		"cover_img" : "https:\/\/img00.yuanxinkangfu.com\/file\/resource\/201811\/1543461141561.jpeg",
# 		"description" : "<p>1、侧卧位，下肢屈髋屈膝，侧方耳垂、肩峰、股骨大转子在一条直线。&nbsp;<\/p><p>2、上方手叉腰防止上斜方肌代偿，维持至出现抖动即放松。<\/p>",
# 		"attentions" : "抬头速度不宜过快。",
# 		"created" : 1525673982,
# 		"updated" : 1545616681
# 	}
# ]}

