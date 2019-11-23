import sqlobject
from sqlobject.mysql import builder

conn = builder()(user='root',
                 passwd='',
                 host='localhost',
                 db='xyl_test')
class PhoneNumber(sqlobject.SQLObject):
    _connection = conn
    number = sqlobject.StringCol(length=14, unique=True)
    owner = sqlobject.StringCol(length=255)
    lastCall = sqlobject.DateTimeCol(default=None)

PhoneNumber.createTable(ifNotExists=True)