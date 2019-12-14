
from tornado import  web
from views import gongsiHandler
list=[
    web.url(r'/adduser', gongsiHandler.AddUser),
]