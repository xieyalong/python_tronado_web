
import  json
class User():
    name='aaa'

u=User()
u.name='bbbb'
map = u.__dict__
map = dict(map)
_str=json.dumps(map)
print(_str)





