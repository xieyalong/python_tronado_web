
from tornado.web import  RequestHandler
import   views.gognsi.用户信息.user_xlsx as ux
from utils import strUtil
#导入模型,连接
from db_sqlalchemy import models,conn
from db_sqlalchemy.models import Cate,Resource
from db_sqlalchemy.conn import  session
#where语法
from sqlalchemy import or_,and_,text
from sqlalchemy.sql import func

if __name__ == '__main__':
    print(']]]]=',strUtil.toJson(ux.mian()))


class  AddUser(RequestHandler):
    def get(self,*args,**kwargs):
        arr=ux.mian()
        list=[]
        for item in  arr:
            self.write('开始<br>')
            self.write('==='+strUtil.toJson(item))
            # self.add(,,,,,)
            u = models.omo_military_user()
            u.user_name = item['user_name']
            u.name = item['name']
            u.type = item['type']
            u.parent_id = item['parent_id']
            u.height = item['height']
            u.weight = item['weight']
            u.birthday = item['birthday']
            list.append(u)
            # 添加数据
            conn.session.add_all(list)
            # 提交数据
            conn.session.commit()
        # self.write(strUtil.toJson(ux.mian()))
        self.write('------------------------')
    def a(self):
        pass
    def add(self,user_name, name, type, parent_id, height, weight, birthday):
        pass
        # u = models.omo_military_user()
        # u.user_name = user_name
        # u.name = name
        # u.type = type
        # u.parent_id = parent_id
        # u.height = height
        # u.weight = weight
        # u.birthday = birthday
        #
        # # 添加数据,如果有此数据就修改，没有此数据就添加
        # conn.session.add(u)
        # # 提交数据
        # conn.session.commit()
