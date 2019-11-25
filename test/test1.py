


class User():
    name=''
    age=0
    id=0
    '''
           定义字典键：
           当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
           但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
    def keys(self):
        return ('name', 'age', 'id')


    '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
    def __getitem__(self, item):
        return getattr(self, item)

import json
u=User()
u.name='张三'
u.age=5
u.id=45
print('对象字段=',u.name)
#输出<__main__.User object at 0x02BE4110>
print('对象地址=',u)
d=dict(u)
print('转字典=',d)
print('字典字段=',d['name'])
print('字典转json=',json.dumps(d,ensure_ascii=False))




