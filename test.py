
from  utils.dbUtil import DBMysql

res=DBMysql.findSingle('select * from xyl_user')
print(res)




