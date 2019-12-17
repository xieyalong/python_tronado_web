
from tornado.web import  RequestHandler
import   views.gognsi.用户信息.user_xlsx as ux
from utils import strUtil
#导入模型,连接
from db_sqlalchemy import models,conn
from db_sqlalchemy.models import Cate,Resource,omo_military_user
from db_sqlalchemy.conn import  session
#where语法
from sqlalchemy import or_,and_,text
from sqlalchemy.sql import func
import  json

if __name__ == '__main__':
    arr = ux.mian()
    print('size=',len(arr))
    # list = []
    index=0
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
        user=session.query(omo_military_user).filter(omo_military_user.user_name==u.user_name).first()
        print('user=',user)
        if None==user:
            #初始密码 123456
            u.pwd='f6e57fba8e73dbe64cc0b298c07206d7'
            conn.session.add(u)
            conn.session.commit()
            index = int(index) + 1
        else:
            print('有数据',u.user_name)
        print('index=', index)

    print('插入完成')







#http://localhost:8000/adduser
class  AddUser(RequestHandler):
    def get(self,*args,**kwargs):
        arr = ux.mian()
        print('size=', len(arr))
        # list = []
        index = 0
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
            user = session.query(omo_military_user).filter(omo_military_user.user_name == u.user_name).first()
            print('user=', user)
            if None == user:
                conn.session.add(u)
                conn.session.commit()
                index = int(index) + 1
            else:
                print('有数据', u.user_name)
            print('index=', index)

        print('插入完成')
        self.write('--------插入完成----------------')

