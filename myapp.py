
#导入tornado 各个模块
from tornado import  web,ioloop,httpserver
#引入视图
from views import index,home
#配置文件
import config

#继承Application，来配置路由
class MyAppliction(web.Application):
    #重写父类的构造函数
    def __init__(self):
        handlers=[
            # 默认走index http://localhost:8080/
            #如果写http://localhost:8080/index会报错
            # 一个路由包含get和post请求，但是得重写post 和get两个函数
            (r'/', index.IndexHandler),
            #请求路径:http://localhost:8080/index2
            (r'/index2', index.IndexHandler2),
            # http: // localhost: 8080 / home
            (r'/home', home.HomeHandler),
            #多层或者根据模块起名字 http://localhost:8080/home/list/
            (r'/home/list/', home.HomeListHandler),
            # 加载html页面
            web.url(r'/html/index.html', index.HtmlHandler),
            # 加载html页面 另一种写法
            web.url(r'/html', index.HtmlHandler),
            #登录接口： http://localhost:8080/login?name=张三&pwd=123456
            #一个路由可以有post和get两种方式
            (r'/login', index.LoginHandler),
            #动态设置相应头部信息，自定义头部信息
            #返回json
            (r'/jsonHeader', index.JsonHeaderHandler),
            #设置默认相应头部信息
            # http: // localhost: 8080 / setHeader
            (r'/setHeader', index.SetHeaderHandler),
            #设置相应状态码
            (r'/statusCode', index.StatusCodeHandler),
            #重定向
            (r'/chongDingXiang', index.ChongDingXiangHandler),
            # 重定向结果页
            (r'/chongDingXiangUrl', index.ChongDingXiangUrlHandler),
            # 错误处理：http://192.168.1.62:8080/error?flag=1
            (r'/error', index.ErrorHandler),
            # 反向解析，推荐使用这种,
            # http://192.168.1.62:8080/fanXingJieXi
            # name属性只是一个url的唯一标识
            #在跳转页面时候尽量使用，如果r'/fanXingJieXi2'修改成别的
            #只要'key_fxjx2'还在，FanXingJieXiHandler还是能找到修改后的url路径
            #具体代码看index.FanXingJieXiHandler，
            #客户端请求还是使用http://192.168.1.62:8080/fanXingJieXi
            web.url(r'/fanXingJieXi', index.FanXingJieXiHandler, name='key_fxjx'),
            web.url(r'/fanXingJieXi2', index.FanXingJieXiHandler, name='key_fxjx2'),
            #url特定的uri路径解析传值,使用正则匹配,
            #http://192.168.1.62:8080/loginUri/com/xyl/login
            #com/xyl/login是三个参数，只要符合正则规则就行
            #也可以是http://192.168.1.62:8080/loginUri/a/b/c
            (r'/loginUri/(\w+)/(\w+)/(\w+)', index.LoginUriHandler),

            #get_query_argument方式获取请求参数
            #post和get
            web.url(r'/query_argument', index.get_query_argumentHandler),
            #登录页面
            web.url(r'/login_html', index.HtmlLoginHandler),
            #请求详情信息获取请求参数
            #请求来的东西 都可以获取
            web.url(r'/requestInfo', index.RequestInfoHandler),
            #上传页面
            web.url(r'/upfile.html', index.UPFileHandler),
            web.url(r'/upfile', index.UPFileHandler),
            #刷新缓冲区，关闭本次请求通道
            web.url(r'/huanCunQu', index.HuanCunQuHandler),
            #请求顺序
            web.url(r'/jieKouShunXu', index.JieKouShunXuHander),
            # 模板-jstl
            web.url(r'/moban.html', home.HomeMoBanHandler),

        ]
        # 映射路由
        #C:\pythonWorkspace\tornaTest02\static
        # print('>]项目目录路径=',config.settings['static_path'])
        #把路由，配置文件数据传给父类
        #**config.settings等价于   super(MyAppliction, self).__init__(handlers=handlers,debug=True,等等)
        #也就是把config['settings']合成一个变量
        super(MyAppliction, self).__init__(handlers=handlers,
                                           **config.settings)
