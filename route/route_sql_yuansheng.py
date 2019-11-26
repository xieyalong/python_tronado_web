from tornado import  web,ioloop,httpserver
from views import index,home,db,db_sqlalchemy
list=[
    # 查询一条和多条
    # http://localhost:8000/findUserById
    web.url(r'/findUserById', db.findUserById),
    # 插入
    web.url(r'/insert', db.insertHandler),
    # 修改
    # http://localhost:8000/update
    web.url(r'/update', db.updateHandler),
    # 删除
    web.url(r'/delete', db.deleteHandler),
    # 联合查询
    # http://localhost:8000/findCateById
    web.url(r'/findCateById', db.findCateByIdHandler),
]