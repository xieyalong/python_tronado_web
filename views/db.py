
from tornado import  web
import json
#导入包
import util.dbUtil as dbutil


#查询1条和多条
class findUserById(web.RequestHandler):

    # get请求
    def get(self):
        # 查询单条
        results =dbutil.DBMysql.findSingle("select * from omo_user where mobile='13960291731'")
        self.write(json.dumps(results))
        self.write('<br>-------------------------------<br>')
        # 查询多条
        results = dbutil.DBMysql.findMulti("select * from omo_user")
        self.write(json.dumps(results))


    def post(self):
        self.write('index2页面post请求')

#插入数据，添加数据
class insertHandler(web.RequestHandler):
    def get(self):
        try:
            sql="insert into xyl_user(uname,upassword,email,age) value  ('谢亚龙','123456','xyl@qq.com',23)"
            dbutil.DBMysql.insert(sql)
            self.write('插入成功')
        except Exception as e:
            print('错误=',e)
            self.write('插入失败')
#修改数据
class updateHandler(web.RequestHandler):
    def get(self):
        try:
            sql="update xyl_user set age=30,uname='张三2' where id=2"
            dbutil.DBMysql.update(sql)
            self.write('修改成功')
        except Exception as e:
            print('错误=',e)
            self.write('修改失败')

#删除数据
class deleteHandler(web.RequestHandler):
    def get(self):
        try:
            sql="delete from xyl_user where id=1"
            dbutil.DBMysql.update(sql)
            self.write('删除成功')
        except Exception as e:
            print('错误=',e)
            self.write('删除失败')


