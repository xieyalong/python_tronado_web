

class User():
    name=''
    age=0
    id=0

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

import json
str='{"name": "张三", "age": 5, "id": 45}'

#json转字典
map=json.loads(str)
# 字典转对象
u=Dict(map)
print(u.name,u.age,u.id)

