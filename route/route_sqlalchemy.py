from tornado import  web,ioloop,httpserver
from views import db_sqlalchemy
list=[
    # 使用sqlalchemy框架操作数据库-创建所有表 http://localhost:8000/creteTable
    web.url(r'/creteTable', db_sqlalchemy.creteTableHandler),
    # deleteAll-删除所有表
    web.url(r'/deleteTable', db_sqlalchemy.deleteTableHandler),
    # add操作
    web.url(r'/addStudent', db_sqlalchemy.addStudentHandler),
    # addAll操作
    web.url(r'/addAllStudent', db_sqlalchemy.addAllStudentHandler),
    # update操作
    web.url(r'/update', db_sqlalchemy.UpdateHandler),
    # update操作
    web.url(r'/update', db_sqlalchemy.UpdateHandler),
    # 各种查询
    web.url(r'/find', db_sqlalchemy.FindHandler),
]