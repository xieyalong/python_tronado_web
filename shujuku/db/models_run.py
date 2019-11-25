
#测试

#导入模型,连接
from shujuku.db import models,conn

if __name__ == '__main__':
    ## 创建所有表
    # models.create_db()
    ## 删除所有表
    # models.delete_db()

    stu = models.Student()
    stu.s_age = 23
    stu.s_name = '李四2'
    stu.title = '标题title'
    # 添加数据
    conn.session.add(stu)
    # 提交数据
    conn.session.commit()