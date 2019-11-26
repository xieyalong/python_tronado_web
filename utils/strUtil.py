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

#list实体bean转成json
#listData=list实体bean
def  listClassToJson(listClass):
    list=[]
    for item in listClass:
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

# josn转实体bean对象
def josnToClass(_str):
    map = json.loads(_str)
    clas=Dict(map)
    return  clas


#json字符串转list实体bean对象
# list=strUtil.josnToListClass(_str)
# print(list[0].cate_name)
def josnToListClass(_str):
    list=[]
    listMap=json.loads(_str)
    for i in range(0,len(listMap)):
        map=Dict(listMap[i])
        list.append(map)
    return list


