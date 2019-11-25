from tornado.web import  RequestHandler
from shujuku.sqlalchemy_models import models


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