
import  time
import  threading



def longIO():
    print('longIO 开始')
    def run():
        print('开始耗时操作')
        time.sleep(5)
        print('结束耗时操作')
    threading.Thread(target=run).start()






# 一个客户端的额请求
def  req01():
    print('开始处理请求req01')
    #休眠3秒
    print('结束处理请求req01')
# 另外一个客户端的额请求
def  req02():
    print('开始处理请求req02')
    print('结束处理请求req02')

#模拟tornado服务器，IOLoop循环读取请求
#如果有一个耗时的，其他的都要等待，效率非常低
def main():
    longIO()
    req01()
    req02()

if __name__ == '__main__':
    main()