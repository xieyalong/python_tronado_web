
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
            # # 添加数据
            # conn.session.add_all(list)
            # # 提交数据
            # conn.session.commit()
        # self.write(strUtil.toJson(ux.mian()))
        self.write('------------------------')

