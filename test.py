
#-------列表简写----------------------
list=[]
list.append({'a':'A'})
list.append({'a':'B'})
list.append({'a':'C'})

list2=[item['a'] for item in list]
print(list2)

# 等价于：
list2=[]
for item in list:
    list2.append(item['a'])
print(list2)







