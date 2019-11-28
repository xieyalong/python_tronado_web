
import  re
import json
# 账号-角色（1=士兵，2=医疗兵）-士兵所属的医疗兵-军衔(上中下士)-等级(军师旅团营)-部队;
path='C://test//1.txt'
#默认utf-8;ignore：忽略错误；自动
with open(path,'r+',encoding='utf-8',errors='ignore') as f:
    _d=f.read()
    _d = re.sub(r'\s', '', _d)
    list=_d.split(';')
    listData=[]
    i=0
    for item in list:
        # if i==0:
        #     continue
        list2=item.split('-')
        if len(list2)>1:
            # print('item-list=', list2, 'len=', len(list2))
            map={
                'user_name':list2[0],
                'role':list2[1],
                'role_parent_id':list2[2],
                'military_rank':list2[3],
                'level':list2[4]
            }
            # print('map=',map)
            listData.append(map)
    _json=json.dumps(listData,ensure_ascii=False)
    print('listData=',_json)

        # for  item2 in list2:
        #     print(item2)
        #     pass


