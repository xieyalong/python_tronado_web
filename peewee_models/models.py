from peewee import *
import datetime

db = MySQLDatabase("xyl_test", host="127.0.0.1", user="root", passwd="",port=3306,charset='utf8')


#查询数据库是连接  #返回false未连接
if(not db.is_closed()):
    db.connect()
else:
    print('已连接')

class BaseModel(Model):
    class Meta:
        database = db

#继承自BaseModel，直接关联db，并且也继承了Model。Model有提供增删查改的函数
#自动添加id列
class User(BaseModel):

    # unique=True 唯一的，如果没有id，系统会自动加上id
    user_ID = IntegerField(unique=True)  # id，学号必须是独一份的，不允许重复
    username = CharField()
    title = TextField()
    # index:索引
    # name = CharField(verbose_name='姓名', max_length=10, null=False, index=True)
    # passwd = CharField(verbose_name='密码', max_length=20, null=False, default='111111')
    # gender = IntegerField(verbose_name='姓别', null=False, default=1)
    # is_admin = BooleanField(verbose_name='是否是管理员', default=False)
    class Meta:
        # db_table指定表名，
        # order_by 指定表中数据的排序顺序,
        # indexes是为表中数据添加索引，加快后续的查询
        # 其中我指定对学生姓名和学号之间建立索引，两个一块查会有速度优势，
        # 后边的True表明，这两个数据组合必须是unique的

        db_table = 'xyl_user'
        # order_by = ('user_ID', 'username', )
        # indexes = (
        #     (('username', 'user_ID'), True),
        # )


class Tweet(BaseModel):
    #外键
    # user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)


from playhouse.migrate import *

# 这是postgresql的，实例化出一个migrator对象
my_db = PostgresqlDatabase(...)
migrator = PostgresqlMigrator(my_db)

# 使用migrate()执行一个或多个操作
# 添加了两个列，删除一个列
title_field = CharField(default='')
status_field = IntegerField(null=True)

migrate(
    migrator.add_column('some_table', 'title', title_field),
    migrator.add_column('some_table', 'status', status_field),
    migrator.drop_column('some_table', 'old_column'),
)


if __name__ == "__main__":
    User.create_table()  # 创建User表
    Tweet.create_table()  # 创建Tweet表
    print('插入成功')