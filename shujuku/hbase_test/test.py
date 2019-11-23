import happybase
conn = happybase.Connection("127.0.0.1", 9090)
print('==============',conn.tables())

# xxx 表示表名，在连接之前要先在终端创建表
# table = conn.table("xxx")

# 创建表---> zhy为表名，info为指定行列为空
conn.create_table('zhy', {"info":{}})

# 删除表--> disable默认为False，删除表的手要修改为True
# conn.delete_table("testtest", True)