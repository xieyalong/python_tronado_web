# 导入pymysql模块
import  pymysql
import  json
import  decimal
import  config

#数据库在增删改后如果不关闭游标和数据库，是查不出来的

# db_sqlalchemy = pymysql.connect(host='39.107.26.185',
#                              user='xieyalong',
#                              password='xieyalong',
#                              database='omo_military',
#                              charset='utf8',
#                              port=3306)
#使用方法
# from  utils.dbUtil import DBMysql
# results = DBMysql.findSingle("select * from omo_user where mobile='13960291731'")
# results = DBMysql.findMulti("select * from omo_user")
class DBMysql():
    db=None
    cursor=None
    #连接数据库
    @staticmethod
    def connet(host,user,password,database,charset,port):
        DBMysql.db=pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             charset=charset,
                             port=port)
        DBMysql.cursor=DBMysql.db.cursor()
        return  DBMysql.db

    #打开数据库
    @staticmethod
    def open():
        DBMysql.connet(host='39.107.26.185',
                              user='xieyalong',
                              password='xieyalong',
                              database='omo_military',
                              charset='utf8', port=3306)
        # DBMysql.connet(host='127.0.0.1',
        #                user='root',
        #                password='',
        #                database='jundui',
        #                charset='utf8', port=3306)

        # db = sqlite3.connect('C:\\test\\com.yxkf.troops.db')

        # DBMysql.connet(host=config.mysql['host'],
        #                user=config.mysql['user'],
        #                password=config.mysql['password'],
        #                database=config.mysql['db1'],
        #                charset=config.mysql['charset'],
        #                port=config.mysql['port'])

    # 断开连接
    @staticmethod
    def close():
        DBMysql.cursor.close()
        DBMysql.db.close()

    # 获取一条数据,返回字段
    @staticmethod
    def findSingle(sql):
        DBMysql.open()
        columns = []
        try:
            # print('cur',DBMysql.cursor)
            #执行sql语句
            DBMysql.cursor.execute(sql)
            #查询结果
            results=DBMysql.cursor.fetchall()
            # 获取表字段
            fields = DBMysql.cursor.description

            # 获取列
            for item in fields:
                columns.append(item[0])

            # 插叙数据
            listData = []

            # 遍历每行数据
            for row in results:
                # (54016, 1637, '3,5,7,8,9', 0, 204, 0, '', 0, 2, 1553841940, 1553841940, '')
                # print('每行的数据',row)
                i = 0
                # 定义Python 字典
                map = {}
                # 遍历没列
                for item in row:
                    map[columns[i]] = item
                    i = i + 1
                # print(map)
                listData.append(map)

            # #关闭
            DBMysql.close()
            return  listData[0]
        except Exception as e:
            print('查询失败'+e)
        return  None
        # 获取一条数据,返回字段

    # 查询多条
    @staticmethod
    def findMulti( sql):
        DBMysql.open()
        columns = []
        try:
            # print('cur', cursor)
            # 执行sql语句
            DBMysql.cursor.execute(sql)
            # 查询结果
            results = DBMysql.cursor.fetchall()
            # 获取表字段
            fields = DBMysql.cursor.description

            # 获取列
            for item in fields:
                columns.append(item[0])

            # 插叙数据
            listData = []

            # 遍历每行数据
            for row in results:
                # (54016, 1637, '3,5,7,8,9', 0, 204, 0, '', 0, 2, 1553841940, 1553841940, '')
                # print('每行的数据',row)
                i = 0
                # 定义Python 字典
                map = {}
                # 遍历没列
                for item in row:
                    map[columns[i]] = item
                    i = i + 1
                # print(map)
                listData.append(map)

            # #关闭
            DBMysql.close()
            return listData
        except Exception as e:
            print('查询失败' + e)
        return None

    #insert into xyl_user(xname,xpassword,email,age) value  ('谢亚龙','123456','xyl@qq.com',23);
    #插入多条数据insert into u1(name,age) values('谢亚龙',45),('张三',90);
    @staticmethod
    def insert(sql):
        try:
            DBMysql.open()
            DBMysql.cursor.execute(sql)
            DBMysql.close()
            return True
        except Exception as e:
            #事务回调
            DBMysql.db.rollback()
            print('插入错误=',e)
            return False

    # update xyl_user set age=30,uname='张三2' where id=2
    @staticmethod
    def update(sql):
        try:
            DBMysql.open()
            DBMysql.cursor.execute(sql)
            DBMysql.close()
            print('update成功')
            return True
        except Exception as e:
            # 事务回调
            DBMysql.db.rollback()
            print('update错误=', e)
            return False

    # delete from xyl_user where id=1;
    @staticmethod
    def delete(sql):
        try:
            DBMysql.open()
            DBMysql.cursor.execute(sql)
            DBMysql.close()
            print('delete成功')
            return True
        except Exception as e:
            # 事务回调
            DBMysql.db.rollback()
            print('delete错误=', e)
            return False
