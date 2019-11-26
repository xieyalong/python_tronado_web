import  os


#相对路径的根目录
base_dirs=os.path.dirname(__file__)
#输出 C:\pythonWorkspace\tornaTest02，当前文件的干目录
print('base_dirs=',base_dirs)



#参数配置
options={
    'port':8000,
    #这是配置的初始化服务器的参数，供服务启动时候调用
    'list':['这是py文件配置端口','a','bdfdfd','ddadsfasdr'],
}

# 配置设置
settings={
    #默认是false=生产模式，
    #debug=true有以下特性：
    #1、true=debug模式
    #2、取消缓存编译的模板（debug=true,compiled_template_cache=true）
    #3、取消缓存静态文件的hash值（debug=true,static_hash_cache=true）
    #4、提供追踪信息，取消=（debug=true,serve_traceback=true）
    #5、自动重启模式=（debug=true,autoreload=true）
    'debug':True,
    #自动重启模式，必须debug=true,
    #如果代码有错误，会启动失败，这时候需要手动重启
    'autoreload':False,
    #取消自动缓存,必须debug=true
    'compiled_template_cache':True,
    #取消hash值，在tornadde css会生成index.css?hash=usidfsdfos,这个也是缓存
    'static_hash_cache':True,
    #一般不会用，是做追踪信息用的
    # 'serve_traceback':True，
    #配置静态文件目录,相对路径，C:\pythonWorkspace\tornaTest02\static
    #尽量避免使用绝对路径
    'static_path':os.path.join(base_dirs,'static'),
    #设置母版（jsp-jstl）目录，
    ## 没有upfile_path，#Application里面没有upfile_path参数
    'template_path':os.path.join(base_dirs,'templates'),

    #关闭自动转义
    'autoescape':None,
}

mysql={
    'host':'127.0.0.1',
    'user':'root',
    'password':'',
    'db1':'jundui',#家里的数据库
    'db2':'omo_military',#公司的数据局
    'charset':'utf8',
    'port':3306
}
