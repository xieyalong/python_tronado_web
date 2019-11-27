
from tornado.web import  RequestHandler


class  IndexCookieHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.write('IndexCookieHandler')
# 设置cookie
class  SetCookieHandler(RequestHandler):
    def get(self,*args,**kwargs):
        #不要使用汉字，不然会报错
        self.set_cookie('aaaa','nnnn')
        self.write('aaaaa')
#获取cookie
class  GetCookieHandler(RequestHandler):
    def get(self,*args,**kwargs):
        #不要使用汉字，不然会报错
        cookie=self.get_cookie('aaaa','msg:未登录')
        # cookie1 = nnnn
        print('cookie1=',cookie)
        cookie = self.get_cookie('bbb', 'msg:未登录')
        # cookie2 = msg:未登录
        print('cookie2=', cookie)
        self.write('cookie=')

# 清除cookie
class  clearCookieHandler(RequestHandler):
    def get(self,*args,**kwargs):
        #path:匹配网址，或者IP地址，多个网站可能有重名的cookie
        # self.clear_cookie('aaaa',path='')
        #清除所有cookie
        self.clear_all_cookies()
        self.write('cookie=')

# 设置安全cookie
class  setSCookieHandler(RequestHandler):
    def get(self,*args,**kwargs):
        #max_age_days:最大天数
        self.set_secure_cookie('aaa','AAAA',max_age_days=30)
        self.write('cookie=')


# 设置安全cookie
class  getSCookieHandler(RequestHandler):
    def get(self,*args,**kwargs):
        #max_age_days:最大天数
        self.set_secure_cookie('aaa','AAAA',max_age_days=31)
        self.write('cookie=')