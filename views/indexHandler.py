
from tornado import  web
import json
import  os
import  config

#默认请求的页面
#http://localhost:8080/
class IndexHandler(web.RequestHandler):
    #get请求
    def get(self,*args,**kwargs):
        global i
        map={'name':'张三','age':4,'msg':'这是index路由'}
        jstr=json.dumps(map,ensure_ascii=False);
        print(jstr)
        #相应给客户端
        self.write('get请求：'+str(jstr))

    #post请求
    def post(self):
        self.write('post请求')


#http://localhost:8080/index2
#用get发送就是get请求
#用post请求就是post请求
class IndexHandler2(web.RequestHandler):
    def initialize(self,a,b):
        pass

    # get请求
    def get(self):
        self.write('index2页面get请求')

    def post(self):
        self.write('index2页面post请求')





#自定义请求头部信息，动态设置请求头部信息
#动态设置头部信息，并返回json数据
class JsonHeaderHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        #设置响应头部，信息在浏览器控制台的Response Headers中显示
        self.set_header('Content-Type','application/json:charset=UTF-8')
        #自定义头部键值对，自定义头部信息
        self.set_header('a','A')


        map = {'name': '张三', 'age': 4, 'msg': '这是用户信息'}
        jstr = json.dumps(map, ensure_ascii=False);
        print(jstr)
        self.write(str(jstr))
        pass

#设置默认的头部信息
class SetHeaderHandler(web.RequestHandler):
    #重写
    def set_default_headers(self):
        self.set_header('Content-Type','text/html:charset=UTF-8')
        pass

    def get(self, *args, **kwargs):
        self.write('get请求修改头部信息')

    def post(self, *args, **kwargs):
        self.write('post请求修改头部信息')


#响应码，状态码，
class StatusCodeHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('返回响应状态码')
        #状态码是正常值，可以不写错误说明
        # self.set_status(200,'错误说明你请求成功了');
        # self.set_status(404);
        # 自定义状态码，必须写错误说明
        #在浏览器General中显示Status Code: 454545 这个说明必须写
        self.set_status(993434, '这个说明必须写：这是自定义状态码');

#重定向到其他url
#redirect=重定向函数
class ChongDingXiangHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        #默认index页面
        # self.redirect('/')
        #页面会重定向到ChongDingXiangUrlHandler里面
        self.redirect('/chongDingXiangUrl')
        pass

#重定向的结果页
class ChongDingXiangUrlHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('这是重定向过来的页面')


#错误处理，请求异常处理，请求错误处理
## http://192.168.1.62:8080/error?flag=1

class ErrorHandler(web.RequestHandler):
    def get(self):
        flag=self.get_query_argument('flag')
        flag=int(flag)
        if 0==flag:
            #send_error后会走write_error()函数
            self.send_error(500)
        self.write('页面加载成功')

    #send_error后调用此方法
    #重写
    def write_error(self, status_code: int):
        #设置状态码
        if 500==status_code:
            self.write('服务器内部错误')
        elif 404==status_code:
            self.write('资源不存在')
        else:
            status_code=8888
            self.write('其他错误')

        self.set_status(status_code)


#反向解析
class FanXingJieXiHandler(web.RequestHandler):
    def get(self):
        #如果r'/fanXingJieXi2'url改了，只要key_fxjx2标识还在，这段代码就不用改
        #作用不是很大
        url = self.reverse_url('key_fxjx2')
        self.write('<a href="' + url + '">跳入反向解析页面<a>')

#反向解析跳入的页面
class FanXingJieXi2Handler(web.RequestHandler):
    def get(self):
        self.write('这是反向解析过来的页面')

#加载html页面
#首先在config里面配置template_path目录
class HtmlHandler(web.RequestHandler):
    def get(self):
        # 默认找的是template_path目录下的
        self.render('index.html')

#加载html页面，登录页面
#首先在config里面配置template_path目录
class HtmlLoginHandler(web.RequestHandler):
    def get(self):
        self.render('login.html')

#=============获取参数，获取请求参数================================
#---------普通传递参数------------
# 提取uri特定部分
# get方式传递数据
# post方式传递数据
# 即可get请求，也能post请求
# 在http请求头中添加自定义的字段



#----获取参数方法详情-------------------

    # get_body_argument()， get_body_arguments(),获取from表单，body里面的数据
    # get_query_argument()获取的是一个值，get_query_arguments() 只能获取headers报头里面的数据
    # get_argument()，get_arguments()  不区分headers报头，post，get传递，from表单，body 都可以获取到
    #对于函数的参数的介绍：
    # get_query_argument(name, default=_ARG_DEFAULT, strip=True)
    # name：获取name属性的值
    # default：设置默认值, 如果没有参数传递过来, 就是用默认值，如果没有name值也没default,会抛出异常
    # strip： True=去除左右空格

    # 注意：
    # 使用上述方法获取参数只能够获取headers报头为
    # "application/x-www-form-urlencoded"或者"multipart/form-data"的数据,

    #  如果想获取json或者xml方式传递的数据需要使用self.request方式获取，
    # 获取方法：
    # self.request.headers.get('Content-Type')获取“application/json”类型传递
    # 获取内容：self.request.body
#-----------------------


#登录接口,获取请求参数
#http://localhost:8080/login?name=张三&pwd=123456

class LoginHandler(web.RequestHandler):
    #接收参数,在http之前调用
    #先执行此函数，在执行get或者post
    #self=this
    def initialize(self):
        name=self.get_argument('name')
        pwd=self.get_argument('pwd')
        print('获取参数',name,pwd)



    # get请求
    def get(self,*args,**kwargs):
        name = self.get_argument('name')
        pwd = self.get_argument('pwd')
        print('get请求get_argument获取 name=', name,'pwd=', pwd)

        map = {'name': '张三', 'age': 40, 'msg': '用户信息'}
        jstr = json.dumps(map, ensure_ascii=False);
        print(jstr)
        # 相应给客户端
        self.write(str(jstr))


    # get请求
    # 用postman请求post都可以获取到
    def post(self):
        name = self.get_argument('name')
        pwd = self.get_argument('pwd')
        print('post获取参数 name=', name,'pwd=', pwd)

        map = {'name': '张三', 'age': 40, 'msg': '用户信息'}
        jstr = json.dumps(map, ensure_ascii=False);
        print(jstr)
        # 相应给客户端
        self.write(str(jstr))


#获取请求参数, uri特定部分参数解析,提取uri特定部分,
#这种情况下用的很少
# url特定的uri路径解析传值,使用正则匹配,
# 路径样式：http://192.168.1.62:8080/loginUri/com/xyl/login
# com/xyl/login是三个参数，只要符合正则规则就行
# 也可以是http://192.168.1.62:8080/loginUri/a/b/c
class LoginUriHandler(web.RequestHandler):
    def get(self,h1,h2,h3):
        # 输出结果为：“uri获取参数= com xyl login”
        print('uri获取参数=',h1,h2,h3)
        self.write('这是uri路径解析,获取的参数='+h1+','+h2+','+h3)
        pass

#获取请求参数,获取客户端请求参数
#使用 get_query_argument和get_query_arguments 获取请求参数,只能获取heders里面的数据
#使用 get_body_argument和get_body_argument获取请求参数，只能获取是from表单和body里面的数据
class get_query_argumentHandler(web.RequestHandler):
    #get请求
    # http://192.168.1.62:8080/query_argument?name=slsss&list=1&list=2
    def get(self):
       name=self.get_query_argument('name')
       list=self.get_query_arguments('list')
       _str=str(json.dumps(list))
       # 输出"slsss,["1", "2"]"
       self.write(name+','+_str)

    # post请求
    #使用from表单（login.html）提交获取的数据,只能用get_body_argument来接收，用get_query_argument接收不到
    def post(self):
        name = self.get_body_argument('name')
        pwd= self.get_body_argument('pwd')
        # list = self.get_query_arguments('list')
        list=[]
        _str = str(json.dumps(list))
        _str=name + ',' + _str+','+pwd
        # 输出"slsss,["1", "2"]"
        self.write(_str)

#-------request对象-------------------
# 获取请求详情信息，获取请求参数
# 请求来的东西 都可以获取
class RequestInfoHandler(web.RequestHandler):
    # http://192.168.1.62:8080/requestInfo?name=aaa&pwd=3333
    def get(self):
        name=self.get_argument('name')
        pwd = self.get_argument('pwd')

        # name = aaa & pwd = 3333 获取请求参数
        print(self.request.query)
        # body里面的请求参数
        print(self.request.body)
        #GET
        print(self.request.method)
        #192.168.1.62:8080
        print(self.request.host)
        #/requestInfo?name=aaa&pwd=3333
        print(self.request.uri)
        # HTTP / 1.1 能使用长连接
        print(self.request.version)
        #服务器ip地址 192.168.1.62
        print(self.request.remote_ip)
        #{}字典类型
        print(self.request.files)
        # 输出请求头信息
        # Host: 192.168.1.62:8080
        # Connection: keep-alive
        # Upgrade-Insecure-Requests: 1
        # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36
        # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
        # Accept-Encoding: gzip, deflate
        # Accept-Language: zh-CN,zh;q=0.9
        print(self.request.headers)
        self.write('这是获取的请求信息')



    #使用login.html from表单提交
    def post(self):
        name = self.get_argument('name')
        pwd = self.get_argument('pwd')

        # name = aaa & pwd = 3333 获取请求参数
        #使用from表单提交，输出为null
        print(self.request.query)
        # body里面的请求参数
        #如果是from表单提交输出b'name=uuuuu&pwd=4444'
        print(self.request.body)
        # GET
        print(self.request.method)
        # 192.168.1.62:8080
        print(self.request.host)
        # /requestInfo?name=aaa&pwd=3333
        print(self.request.uri)
        # HTTP / 1.1 能使用长连接
        print(self.request.version)
        # 服务器ip地址 192.168.1.62
        print(self.request.remote_ip)
        # 上传的文件，字典类型
        print(self.request.files)
        # 输出请求头信息
        # Host: 192.168.1.62:8080
        # Connection: keep-alive
        # Upgrade-Insecure-Requests: 1
        # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36
        # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
        # Accept-Encoding: gzip, deflate
        # Accept-Language: zh-CN,zh;q=0.9
        print(self.request.headers)
        self.write('这是获取的请求信息')


#-------torna.httputil.HTTPFile对象-------------------
# torna.httputil.HTTPFile：是接收上传的文件，上传一个就会产生一个对象
# 属性：
# filename：文件的名字
# body：文件的内容，二进制内容
#content_type:文件的类型，是否是图片等

#上传文件，上传图片，图片上传上传文件和图片,获取上传图片参数
class UPFileHandler(web.RequestHandler):
    #上传页面
    def get(self):
        self.render('upfile.html')
        pass

    #获取的上传的文件
    def post(self):
        # 是字典类型
       filesMap=self.request.files
       # 输出
       # {
       #   'file': [{'filename': '1.txt', 'body': b'\xe9\x98\xbf\xe5\x95\x8a\xe5\xae\x9d\xe5\xae\x9d', 'content_type': 'text/plain'},
        #          {'filename': '2.txt', 'body': b'\xe9\x98\xbf\xe5\x95\x8a\xe5\xae\x9d\xe5\xae\x9d', 'content_type': 'text/plain'}],
       #  'img': [{'filename': 'img1.jpg', 'body': b'\xe9\x98\xbf\xe5\x95\x8a\xe5\xae\x9d\xe5\xae\x9d', 'content_type': 'image/jpeg'}]
       #  }
       # 'file','img':是<input type="file" name="file" value="选择文件"/>和<input type="file"  name="img" value="选择图片"/>
       # 里面是list，name="file"可以是多个

       #{'filename': '1.txt' 上传的文件名称
       # 'content_type': 'text/plain' 文案类型
       # 'body':二进制内容

        # 输出
        # 文件名称=1.txt
        # 文件名称=2.txt
        # 图片名称=img1.jpg
       print('文件名称='+filesMap['file'][0]['filename'])
       print('文件名称=' + filesMap['file'][1]['filename'])
       print('图片名称='+filesMap['img'][0]['filename'])
       print('config.base_dirs='+config.base_dirs)


       # 把文件上传到upfile里面
       root_pth=os.path.join(config.base_dirs+'/upfile/')
       # 保存txt文件
       with open(os.path.join(root_pth+filesMap['file'][0]['filename']),'wb') as f:
            f.write(filesMap['file'][0]['body'])

       with open(os.path.join(root_pth + filesMap['file'][1]['filename']), 'wb') as f:
            f.write(filesMap['file'][1]['body'])

       # 保存图片
       with open(os.path.join(root_pth+filesMap['img'][0]['filename']), 'wb') as f:
           f.write(filesMap['img'][0]['body'])

       self.write('上传成功')


#缓冲区
class HuanCunQuHandler(web.RequestHandler):
    def get(self):
        #write会连续输出一直到finish结束为止
        self.write('1')
        self.write('2')
        self.write('c')
        #关闭本次请求通道，刷新缓冲区到页面
        self.finish()
        self.write('此行不会被运行')

#接口调用顺序
#在正常情况下：set_default_headers-》initialize-》prepare-》get-》on_finish
#在有错误情况下：set_default_headers-》initialize-》get（里面如果错误）-》set_default_headers-》write_error-》on_finish
class JieKouShunXuHander(web.RequestHandler):
    #最先调用，设置头部
    def set_default_headers(self):
        print('set_default_headers')
    # 在http请求之前调用
    def initialize(self):
        print('initialize')
        pass
    # 任何一个http请求都会执行
    def prepare(self):
        print('prepare')
        pass
    def get(self):
        print('get')
        #测试错误情况下
        self.send_error(500)
        #正常情况下输出
        # self.write('JieKouShunXuHander')
    def post(self):
        print('post')
        pass

    def write_error(self, status_code, **kwargs):
        print('write_error')
    #最后运行
    #1、释放内存
    #2、记录日志
    #3、不要在此方法中写self.write(),不要给客户端响应
    #只是做服务器内部的事情
    def on_finish(self):
        print('on_finish')
        pass



