

class Test:
    #直接通过类可以调用
    name='aaa'

    #@staticmethod表名是静态方法
    @staticmethod
    def testRun():
        return '静态方法@staticmethod注解并且不带self'
