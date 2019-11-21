
from tornado import  web

class HomeHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        #相应给客户端
        self.write('home页面')


#多层或者根据模块起名字 http://192.168.1.62:8080/home/list/
class HomeListHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        #相应给客户端
        self.write('HomeList页面')