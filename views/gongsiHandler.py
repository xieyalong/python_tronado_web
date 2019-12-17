
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
import  json

if __name__ == '__main__':
    arr = ux.mian()
    print(type(arr))
    list = []
    for item in arr:
        print('itme=', item)
        # self.write('==='+strUtil.toJson(item))
        # self.add(,,,,,)
        u = models.omo_military_user()
        u.user_name = str(item['user_name'])
        u.name = str(item.get('name'))
        u.type = int(item['type'])
        u.parent_id = str(item['parent_id'])
        u.height = float(item['height'])
        u.weight = float(item['weight'])
        u.birthday = int(item['birthday2'])
        list.append(u)

    print('listData=', len(list))
    # 添加数据
    conn.session.add_all(list)
    # # 提交数据
    conn.session.commit()




#http://localhost:8000/adduser
class  AddUser(RequestHandler):
    def get(self,*args,**kwargs):
        arr=ux.mian()
        print(type(arr))
        list=[]
        for item in  arr:
            print('itme=',item)
            # self.write('==='+strUtil.toJson(item))
            # self.add(,,,,,)
            u = models.omo_military_user()
            u.user_name = item['user_name']
            u.name = item.get('name')
            u.type = item['type']
            u.parent_id = item['parent_id']
            u.height = item['height']
            u.weight = item['weight']
            u.birthday = item['birthday']
            list.append(u)

        print('listData=', len(list))
        # 添加数据
        conn.session.add_all(list)
        # # 提交数据
        conn.session.commit()
        # self.write(strUtil.toJson(ux.mian()))
        self.write('------------------------')

