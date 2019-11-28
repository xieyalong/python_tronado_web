import  time
import  threading

#callback的的传递流程：callback-》子线程-》run
def longIO(callback):
    print('longIO 开始')
    def run(cb):
        print('开始耗时操作')
        time.sleep(5)
        print('结束耗时操作')
        cb('子线程结束')
    threading.Thread(target=run,args=(callback,)).start()


def callback(data):
    print('这是回到函数=',data)


def test(cb):
    print('回到函数开始')
    cb('这是test')
    print('回调函数结束')


if __name__ == '__main__':
    test(cb=callback)
