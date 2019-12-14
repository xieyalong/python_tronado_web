
from tornado.web import  RequestHandler
import   views.gognsi.用户信息.user_xlsx as ux

class  AddUser(RequestHandler):
    def get(self,*args,**kwargs):
        # self.write(ux.mian())
        self.write('aaaaaaaaaaaaaaaaaaa')
