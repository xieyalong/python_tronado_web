
#说明：使用sqlalchemy框架操作数据库

from tornado.web import  RequestHandler
#引入模型，数据库连接
from shujuku.db import models,conn


#创建所有表
class creteTableHandler(RequestHandler):
    def get(self):
        models.create_db()
        self.write('成功')

#删除所有表
class deleteTableHandler(RequestHandler):
    def get(self):
        models.delete_db()
        self.write('成功')


#增加数据所有表
class addStudentHandler(RequestHandler):
    def get(self):
        try:
            #创建数据
            stu=models.Student()
            stu.s_age=45
            stu.s_name='李四66'
            stu.title='标题title'
            #添加数据
            conn.session.add(stu)
            #提交数据
            conn.session.commit()
            self.write('成功')
        except Exception as e:
            self.write('失败e='+e)
