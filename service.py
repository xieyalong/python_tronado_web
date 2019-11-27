

#导入tornado 各个模块
from tornado import  web,ioloop,httpserver
import tornado
#引入配置文件
import  config
#引入路由模块
import  myapp


# 主入口
if __name__ == '__main__':
    app=myapp.MyAppliction()
    #创建一个服务,让app去匹配路由，处理请求
    hs=httpserver.HTTPServer(app)
    #获取定义的端口
    post=config.options['port']
    arr=config.options['list']
    print('输出配置文件的端口=',post,'---配置的参数list=',arr)

    hs.bind(post)
    #启动10个进程，处理请求,在liunx下不会报错，但在windows下会报错
    #tornado就是使用在linux下的web服务器，因为借助liunx的IOLoop
    #关闭服务器使用tornado.process.fork_processes(),在windows下会报错
    # hs.start(10)
    #在windows下启动
    hs.start()
    #开启loop读取epoll的存储的请求信息
    ioloop.IOLoop.current().start()
    print('此程序不会走')

