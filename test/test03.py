
import json
from  utils import strUtil
class User():
    name=''
    age=0
    id=0




u=User()
u.name='张三'
u.age=5
u.id=45
print(strUtil.classToJson(u))

str='{"name": "张三", "age": 5, "id": 45}'

print(strUtil.josnToClass(u))

