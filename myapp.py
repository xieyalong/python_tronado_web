
#导入tornado 各个模块
from tornado import  web,ioloop,httpserver,process
#引入视图
from views import indexHandler,homeHandler,dbHandler,dbSqlalchemyHandler,gongsiHandler
from route import routeSqlalchemy,routeSql,routeCookie,routeGongsi
#配置文件
import config
import  os
#继承Application，来配置路由
class MyAppliction(web.Application):
    #重写父类的构造函数
    def __init__(self):
        handlers=[
            # 默认走index http://localhost:8080/
            #如果写http://localhost:8080/index会报错
            # 一个路由包含get和post请求，但是得重写post 和get两个函数
            (r'/', indexHandler.IndexHandler),
            #请求路径:http://localhost:8080/index2
            #{'a':'','b':''} 传递是死的请求参数,但必须有initialize来接收
            (r'/index2', indexHandler.IndexHandler2, {'a': '', 'b': ''}),
            # http: // localhost: 8080 / home
            (r'/home', homeHandler.HomeHandler),
            #多层或者根据模块起名字 http://localhost:8080/home/list/
            (r'/home/list/', homeHandler.HomeListHandler),
            # 加载html页面
            web.url(r'/html/index.html', indexHandler.HtmlHandler),
            # 加载html页面 另一种写法
            web.url(r'/html', indexHandler.HtmlHandler),
            #登录接口： http://localhost:8080/login?name=张三&pwd=123456
            #一个路由可以有post和get两种方式
            (r'/login', indexHandler.LoginHandler),
            #动态设置相应头部信息，自定义头部信息
            #返回json
            (r'/jsonHeader', indexHandler.JsonHeaderHandler),
            #设置默认相应头部信息
            # http: // localhost: 8080 / setHeader
            (r'/setHeader', indexHandler.SetHeaderHandler),
            #设置相应状态码
            (r'/statusCode', indexHandler.StatusCodeHandler),
            #重定向
            (r'/chongDingXiang', indexHandler.ChongDingXiangHandler),
            # 重定向结果页
            (r'/chongDingXiangUrl', indexHandler.ChongDingXiangUrlHandler),
            # 错误处理：http://192.168.1.62:8080/error?flag=1
            (r'/error', indexHandler.ErrorHandler),
            # 反向解析，推荐使用这种,
            # http://192.168.1.62:8080/fanXingJieXi
            # name属性只是一个url的唯一标识
            #在跳转页面时候尽量使用，如果r'/fanXingJieXi2'修改成别的
            #只要'key_fxjx2'还在，FanXingJieXiHandler还是能找到修改后的url路径
            #具体代码看index.FanXingJieXiHandler，
            #客户端请求还是使用http://192.168.1.62:8080/fanXingJieXi
            web.url(r'/fanXingJieXi', indexHandler.FanXingJieXiHandler, name='key_fxjx'),
            web.url(r'/fanXingJieXi2', indexHandler.FanXingJieXiHandler, name='key_fxjx2'),
            #url特定的uri路径解析传值,使用正则匹配,
            #http://192.168.1.62:8080/loginUri/com/xyl/login
            #com/xyl/login是三个参数，只要符合正则规则就行
            #也可以是http://192.168.1.62:8080/loginUri/a/b/c
            (r'/loginUri/(\w+)/(\w+)/(\w+)', indexHandler.LoginUriHandler),

            #get_query_argument方式获取请求参数
            #post和get
            web.url(r'/query_argument', indexHandler.get_query_argumentHandler),
            #登录页面
            web.url(r'/login_html', indexHandler.HtmlLoginHandler),
            #请求详情信息获取请求参数
            #请求来的东西 都可以获取
            web.url(r'/requestInfo', indexHandler.RequestInfoHandler),
            #上传页面
            web.url(r'/upfile.html', indexHandler.UPFileHandler),
            web.url(r'/upfile', indexHandler.UPFileHandler),
            #刷新缓冲区，关闭本次请求通道
            web.url(r'/huanCunQu', indexHandler.HuanCunQuHandler),
            #请求顺序
            web.url(r'/jieKouShunXu', indexHandler.JieKouShunXuHander),
            # 模板-jstl
            web.url(r'/moban.html', homeHandler.HomeMoBanHandler),

 # ------------------使用原生操作数据库--------------------------------------------------------
 #            #查询一条和多条
 #            #http://localhost:8000/findUserById
 #            web.url(r'/findUserById',db.findUserById),
 #            #插入
 #            web.url(r'/insert', db.insertHandler),
 #            #修改
 #            #http://localhost:8000/update
 #            web.url(r'/update', db.updateHandler),
 #            #删除
 #            web.url(r'/delete', db.deleteHandler),
 #            #联合查询
 #            #http://localhost:8000/findCateById
 #            web.url(r'/findCateById', db.findCateByIdHandler),
#------------------使用sqlalchemy框架操作数据库--------------------------------------------------------
            # #使用sqlalchemy框架操作数据库-创建所有表 http://localhost:8000/creteTable
            # web.url(r'/creteTable', db_sqlalchemy.creteTableHandler),
            # # deleteAll-删除所有表
            # web.url(r'/deleteTable', db_sqlalchemy.deleteTableHandler),
            # # add操作
            # web.url(r'/addStudent', db_sqlalchemy.addStudentHandler),
            # # addAll操作
            # web.url(r'/addAllStudent', db_sqlalchemy.addAllStudentHandler),
            # #update操作
            # web.url(r'/update', db_sqlalchemy.UpdateHandler),
            # # update操作
            # web.url(r'/update', db_sqlalchemy.UpdateHandler),
            # #各种查询
            # web.url(r'/find', db_sqlalchemy.FindHandler),

            #默认index.html路径，这里不知道为啥找不到index.html,还是第一行使用自己写的默认路由好用
            #StaticFileHandler是系统提供的，专门给静态文件提供的一个路由
            # 要放在最后，因为(.*)$匹配了所欲
            #告诉StaticFileHandler找静态文件去“static/html”下面找
            #默认http://localhost:8000/=index.html,
            # 如果写http://localhost:8000/admin.html，去招admin.html
            # (r'/', web.StaticFileHandler,{'path':os.path.join(config.base_dirs+'/static/html'),'default_filename':'index.html'}),
        ]
        # -----使用原生操作数据库---------
        handlers.extend(routeSql.list)
        # -----使用sqlalchemy框架操作数据库-------------
        handlers.extend(routeSqlalchemy.list)
        # -----cookie操作-------------
        handlers.extend(routeCookie.list)
        handlers.extend(routeGongsi.list)

        # print('ospath='+os.path.join(config.base_dirs+'/static/html'))
        # 映射路由
        #C:\pythonWorkspace\tornaTest02\static
        # print('>]项目目录路径=',config.settings['static_path'])
        #把路由，配置文件数据传给父类
        #**config.settings等价于   super(MyAppliction, self).__init__(handlers=handlers,debug=True,等等)
        #也就是把config['settings']合成一个变量
        super(MyAppliction, self).__init__(handlers=handlers,
                                           **config.settings)
