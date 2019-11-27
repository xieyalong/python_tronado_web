
from tornado import  web
from views import cookieHandler
list=[
    web.url(r'/indexCookie', cookieHandler.IndexCookieHandler),
    web.url(r'/setCookie', cookieHandler.SetCookieHandler),
    web.url(r'/getCookie', cookieHandler.GetCookieHandler),
]