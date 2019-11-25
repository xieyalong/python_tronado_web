
#测试

import  json
#导入模型,连接
from shujuku.db_sqlalchemy import models,conn
from shujuku.db_sqlalchemy.models import Student,Cate

#where语法
from sqlalchemy import  not_,or_,and_


#添加一条
def add():
    stu = models.Student()
    stu.s_age = 23
    stu.s_name = '李四2'
    stu.title = '标题title'
    # 添加数据,如果有此数据就修改，没有此数据就添加
    conn.session.add(stu)
    # 提交数据
    conn.session.commit()

#添加多条
def addAll():
    try:
        stus = []
        # 创建数据
        stu = models.Student()
        stu.s_age = 45
        stu.s_name = '李四9'
        stu.title = '标题title'
        stus.append(stu)
        stu2 = models.Student()
        stu2.s_age = 45
        stu2.s_name = '李四8'
        stu2.title = '标题title'
        stus.append(stu2)
        # 添加数据
        conn.session.add_all(stus)
        # 提交数据
        conn.session.commit()
        print('成功')
    except Exception as e:
        print('失败e=' + e)


#使用会话删除一条数据
def delete():
    try:
        # 查询第一条数据
        stu = conn.session.query(models.Student).filter(models.Student.s_name == '李四9').first()
        print('stu=',stu)
        if stu!=None:
            conn.session.delete(stu)
            conn.session.commit()
            print('删除成功')
        else:
            print('数据不存在')
    except Exception as e:
        print('e=',e)


#修改部分字段,推荐使用这个
def update1():
    stu = conn.session.query(models.Student).filter(models.Student.s_name == '李四2').first()
    if stu !=None:
        stu.s_name='张三'
        stu.title = '李四修改为张三，使用add方法修改'
        # add 有此数据就修改，没此数据就添加
        conn.session.add(stu)
        conn.session.commit()
        print('修改成功')
    else:
        print('数据不存在')

#修改，不推荐,使用字典
def update2():
    stu = conn.session.query(models.Student).filter(models.Student.s_name == '张三')
    stu.update({'s_name':'李四','title':'张三改回了李四'})
    conn.session.commit()

def find():
    # https://www.cnblogs.com/robertx/p/11122851.html
    list=conn.session.query(Cate).all()
    print('查询所有', len(list))



    # #sqlalchemy框架原生写法
    # stu= conn.session.query(models.Student).filter(models.Student.s_name=='李四').all()
    #
    # print('all=',stu)
    # #转json错误
    # # print('stu=', json.dumps(stu))
    #
    # #查询第一条数据
    # stu = conn.session.query(models.Student).filter(models.Student.s_name == '李四8').first()
    # print('first=', stu)







if __name__ == '__main__':

    ## 创建所有表
    # models.create_db()
    ## 删除所有表
    # models.delete_db()
    # add()
    find()
    # delete()
    # delete2()
    # update1()
    # update2()
    pass
