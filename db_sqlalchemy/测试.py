
#测试

#导入模型,连接
from db_sqlalchemy import models,conn
from db_sqlalchemy.models import Cate,Resource
from db_sqlalchemy.conn import  session
#where语法
from sqlalchemy import or_,and_,text
from sqlalchemy.sql import func
from utils import strUtil

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

#-----------查询所有-----------------------
    #“all()”的使用
    list= conn.session.query(Cate).all()
    print('查询所有 size=', len(list))
    print('查询所有 size=', strUtil.listClassToJson(list))
    # for item in list:
    #     print('map=',strUtil.classToJson(item))


# -----------查询一条-----------------------
    # “filter()”条件筛查
    #一个条件的筛查，获取所有
    # Cate.id=类直接调用参数,用的是>=,==等
    list = session.query(Cate).filter(Cate.id >= 2).all()
    print('条件筛查 =', len(list))



    #“first()”获取第一条数据，获取一条数据
    cate = session.query(Cate).filter(Cate.id >= 2).first()
    print('取出一条数据 cate=',cate.cate_name)
# -----------and查询------------------------
    #“and_”使用
    _and=and_(Cate.id > 3, Cate.cate_name == '颈部',Cate.type==1)
    ret = session.query(Cate).filter(_and).all()
    print('and使用 size=',len(ret))
# -----------or查询--------------------------
    #“or_”使用
    _or=or_(Cate.id > 3, Cate.cate_name == '颈部',Cate.cate_name=='肩部',Cate.type==1)
    ret = session.query(Cate).filter(_or).all()
    print('or使用 size=', len(ret))
# -----------制定列表查询--------------------------
    # 3. 查询数据,指定查询数据列加入别名
    #User.name.label('username')username=数据库字段，name=实体类字段
    # 查询数据, 指定查询数据列加入别名
    # r3 = session.query(User.name.label('username'), User.id).firset()
    _and=and_(Cate.id > 3, Cate.cate_name == '颈部',Cate.type==1)
    ret = session.query(Cate.cate_name, Cate.id,Cate.parent_id).filter(_and).all()
    print('指定列名查询=',len(ret))
# -----------sql语句查询-原生查询------------------------
    # 原生sql查询 多个条件
    ret = session.query(Cate).from_statement(text("select * from omo_pe_cate where cate_name=:name and type=:type")).params({'name': '颈部', 'type': '1'}).all()
    print('原生查询1 size=',len(ret))

    # 原生sql查询 多个条件
    ret = session.query(Cate).from_statement(
        text("select * from omo_pe_cate where cate_name=:name and  type=:type or cate_name=:name2")).params(
        {'name': '颈部', 'type': '1','name2':'肩部'}).all()
    print('原生查询2 size=', len(ret))

    # 原生sql查询 一个条件，一个条件禁止使用字典，不然报错
    ret = session.query(Cate).from_statement(
        text("select * from omo_pe_cate where cate_name=:name1")).params(name1='颈部').all()
    print('原生查询3 size=', len(ret))

# -----------联合查询---sql语句查询-原生查询---------------
    # 联合查询，联查
    _and = and_(Cate.cate_name == '颈部')
    ret = session.query(Cate).join(Resource, Cate.id == Resource.cate_id).filter(_and).all()
    print('联查查询 size=', len(ret))

    # 原生sql 联查-联合查询
    ret = session.query(Cate, Resource).from_statement(
        text(
            "select * from omo_pe_cate as cate inner join omo_resource as r on cate.id=r.cate_id where cate.cate_name='颈部'")).all()
    print('原生联合查询4 size=', len(ret))

    # 原生sql inner join联查 一个条件
    ret = session.query(Cate, Resource).from_statement(
        text(
            "select * from omo_pe_cate as cate inner join omo_resource as r on cate.id=r.cate_id where cate.cate_name=:cate_name")).params(
        cate_name='颈部').all()
    print('原生联合查询5 size=', len(ret))

    # 原生sql inner join联查 多个条件
    ret = session.query(Cate, Resource).from_statement(
        text(
            "select * from omo_pe_cate as cate inner join omo_resource as r on cate.id=r.cate_id where cate.cate_name=:cate_name and cate.type=:type and  r.id>:id")).params(
        {'cate_name': '颈部', 'type': '1', 'id': '15'}).all()
    print('原生查询6 size=', len(ret))

# -----------排序-倒序-------------------
    # 排序order_by
    _or = or_(Cate.id > 3, Cate.cate_name == '颈部', Cate.cate_name == '肩部', Cate.type == 1)
    ret = session.query(Cate).order_by(Cate.id.desc()).filter(_or).all()
    print('倒序 size=', len(ret))
# -----------区间查询-------------------
    #  between 查询大于1小于3的
    ret = session.query(Cate).filter(Cate.id.between(1, 3),  Cate.cate_name == '肩部').all()
    print('区间查询1 size=', len(ret))

    # "between" 查询大于1小于3的
    _or = or_(Cate.id > 3, Cate.cate_name == '颈部', Cate.cate_name == '肩部', Cate.type == 1)
    ret = session.query(Cate).filter(Cate.id.between(1, 3), _or).all()
    print('区间查询2 size=', len(ret))
# -----------in_查询-------------------
    # "in"查询id等于1,3,4的
    _in = Cate.id.in_([1, 3, 4])
    ret = session.query(Cate).filter(_in).all()
    print('in查询1 size=', len(ret))


    # "in"查询id等于1,3,4的
    _in=Cate.id.in_([1, 3, 4])
    _or = or_(Cate.id > 3, Cate.cate_name == '颈部', Cate.cate_name == '肩部', Cate.type == 1)
    ret = session.query(Cate).filter(_in,_or).all()
    print('in查询2 size=', len(ret))
# -----------模糊查询-------------------
    #模糊查询
    ret = session.query(Resource).filter(Resource.resource_name.like('%八段锦%')).all()
    print('模糊查询1 size=', len(ret))


    # 模糊查询
    _or = or_(Resource.type == 1,Resource.cate_id==3)
    ret = session.query(Resource).filter(Resource.resource_name.like('%八段锦%'),_or).all()
    print('模糊查询2 size=', len(ret))
# -----------函数查询-------------------
    #获取最大的数，最大函数
    ret = session.query(func.max(Resource.id)).first()
    #输出(2195,)
    print('max函数=',ret)

    # 获取最小的数，最小函数
    ret = session.query(func.min(Resource.id)).first()
    # 输出(1,)
    print('min函数=', ret)

    # 求和函数,sum函数
    ret = session.query(func.sum(Resource.id)).first()
    # 输出(Decimal('2352586'),)
    print('sum函数=', ret)

    # 获取总条数
    ret = session.query(func.count(Resource.id)).first()
    # 输出(2112,)
    print('count函数=', ret)
# -----------分组查询--------------------
    #分组查询-报错
    # ret = session.query(Resource).group_by(Resource.type).all()
    # print('分组查询1', ret)

    # 分组查询
    ret = session.query(
        func.max(Resource.id),
        func.sum(Resource.id),
        func.min(Resource.id)).group_by(Resource.type).having(func.min(Resource.id) > 2).all()
    print('分组查询1', ret)

    # -----------子查询-------------------

    # 子查询
    zi_sql=session.query(Cate.id).filter(Cate.id==1)#子语句
    _in=Resource.cate_id.in_(zi_sql)#in 语句
    ret = session.query(Resource).filter(_in).all()
    print('子查询 size=', len(ret))

def find2():
    ret=session.query(Cate).filter(Cate.cate_name=='颈部').all()
    _str =strUtil.listClassToJson(ret)
    print('转json=',_str)
    list=strUtil.josnToListClass(_str)
    print('转list实体bean=', list)
    for cate in list:
        print(cate.cate_name)







def add(age,user_name,name,type,parent_id,height,weight,birthday):
    u = models.omo_military_user()
    u.age
    u.user_name=user_name
    u.name=name
    u.type=type
    u.parent_id=parent_id
    u.height=height
    u.weight=weight
    u.birthday=birthday

    # 添加数据,如果有此数据就修改，没有此数据就添加
    conn.session.add(u)
    # 提交数据
    conn.session.commit()

if __name__ == '__main__':
    add(1, '1', '1', 1, '1', 1, 1,'1')
    ## 创建所有表
    # models.create_db()
    ## 删除所有表
    # models.delete_db()
    # add()
    # delete()
    # delete2()
    # update1()
    # update2()
    # find()
    # find2()
    
    pass
