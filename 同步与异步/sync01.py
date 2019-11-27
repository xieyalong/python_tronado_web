
import  time
# 一个客户端的额请求
def  req01():
    print('开始处理请求req01')
    print('结束处理请求req01')
# 另外一个客户端的额请求
def  req02():
    print('开始处理请求req02')
    print('结束处理请求req02')

#模拟tornado服务器，IOLoop循环读取请求
def main():
    req01()
    req02()
    while 1:
        time.sleep(0.1)
        pass

if __name__ == '__main__':
    main()