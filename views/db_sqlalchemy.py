from tornado.web import  RequestHandler
from shujuku.sqlalchemy_models import models
class creteTableHandler(RequestHandler):
    def get(self):
        models.create_db()
        self.write('成功')