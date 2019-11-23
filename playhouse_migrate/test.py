
from playhouse.migrate import *
from peewee_models import  models


# pip install Postgres
db = MySQLDatabase("xyl_test", host="127.0.0.1", user="root", passwd="",port=3306,charset='utf8')
db.connect()
# 这是postgresql的，实例化出一个migrator对象
my_db = PostgresqlDatabase(db)
migrator = PostgresqlMigrator(my_db)

# 使用migrate()执行一个或多个操作
# 添加了两个列，删除一个列
title_field = CharField(default='')
status_field = IntegerField(null=True)

migrate(
    migrator.add_column('xyl_user', 'title', title_field),
    migrator.add_column('xyl_user', 'status', status_field),
    migrator.drop_column('xyl_user', 'username'),
)
