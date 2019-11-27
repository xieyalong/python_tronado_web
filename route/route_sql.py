from tornado import  web,ioloop,httpserver
from views import indexHandler,homeHandler,dbHandler,dbSqlalchemyHandler
list=[
    # 查询一条和多条
    # http://localhost:8000/findUserById
    web.url(r'/findUserById', dbHandler.findUserById),
    # 插入
    web.url(r'/insert', dbHandler.insertHandler),
    # 修改
    # http://localhost:8000/update
    web.url(r'/update', dbHandler.updateHandler),
    # 删除
    web.url(r'/delete', dbHandler.deleteHandler),
    # 联合查询
    # http://localhost:8000/findCateById
    web.url(r'/findCateById', dbHandler.findCateByIdHandler),
]