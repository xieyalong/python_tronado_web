
from  mysql_util.dbUtil import DBMysql

res=DBMysql.findSingle('select * from xyl_user')
print(res)




