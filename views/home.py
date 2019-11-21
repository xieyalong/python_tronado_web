
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


class HomeMoBanHandler(web.RequestHandler):
    def get(self):
        _num=3
        #"aa":名字随便起的，但是html中也要写“aa”
        # self.render('moban.html',num=_num)
        self.render('moban.html')
        # self.write('HomeMoBanHandler')