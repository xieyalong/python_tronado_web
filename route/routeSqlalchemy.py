from tornado import  web,ioloop,httpserver
from views import dbSqlalchemyHandler
list=[
    # 使用sqlalchemy框架操作数据库-创建所有表 http://localhost:8000/creteTable
    web.url(r'/creteTable', dbSqlalchemyHandler.creteTableHandler),
    # deleteAll-删除所有表
    web.url(r'/deleteTable', dbSqlalchemyHandler.deleteTableHandler),
    # add操作
    web.url(r'/addStudent', dbSqlalchemyHandler.addStudentHandler),
    # addAll操作
    web.url(r'/addAllStudent', dbSqlalchemyHandler.addAllStudentHandler),
    # update操作
    web.url(r'/update', dbSqlalchemyHandler.UpdateHandler),
    # update操作
    web.url(r'/update', dbSqlalchemyHandler.UpdateHandler),
    # 各种查询
    web.url(r'/find', dbSqlalchemyHandler.FindHandler),
]