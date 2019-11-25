import  json
import ast
########################
#python类型转json
def toJson(obj):
    return json.dumps(obj,ensure_ascii=False)
########################
#json转list
def josnToList(jsonList):
    return json.loads(jsonList)
########################
#json转map
def josnToDict(jsonDict):
    return json.loads(jsonDict)
########################
#obj转字符串
def toStr(obj):
    return str(obj)
#字符串转map
def strToDict(str):
    return ast.literal_eval(str)
########################
#字符串转map
def strToList(str):
    return ast.literal_eval(str)
########################
#list转元组
def listToTuple(obj):
    return tuple(obj)
########################
#list元组转map [('Bdpagetype', '1')]
def listTupletoDict(listTuple):
    return dict(listTuple)
########################
#元组转list
def tupleToList(obj):
    return list(obj)





#实体类转json
# class User():
#     name=''
#
# u=User()
# u.name='aaa'
#
# map={'A':'a'}
# print('wwww=',map.get('b'))
# print(strUtil.classToJson(u))

def classToJson(objClass):
    map = objClass.__dict__
    map = dict(map)
    #从数据库查询，去掉_sa_instance_state
    if None!=map.get('_sa_instance_state'):
        del map['_sa_instance_state']
        map = dict(map)

    str_ = json.dumps(map,ensure_ascii=False)
    return str_

#实体bean list转成json
def  listClasToJson(listData):
    list=[]
    for item in listData:
        map = item.__dict__
        map = dict(map)
        # 从数据库查询，去掉_sa_instance_state
        if None != map.get('_sa_instance_state'):
            del map['_sa_instance_state']
            map = dict(map)
        list.append(map)
    return  json.dumps(list,ensure_ascii=False)

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__



def josnToClass(jsonStr):
    map = strToDict(jsonStr)
    print('map==',map)
    return  Dict(map)


