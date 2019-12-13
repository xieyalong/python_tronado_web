
from openpyxl import load_workbook
import  config
import  json

list_fenzu=[]
#解析分组
def fenzu(sheet):
    i = 0
    # print('sheet名称=', sheet)
    # print('根据坐标获取=',sheet['A1'].value,sheet['B1'].value)
    # print('根据坐标获取=', sheet['A2'].value, sheet['B2'].value)

    rows = sheet.rows
    # print(rows)
    title = [];
    listData=[]
    index = 0
    # 迭代所有的行
    for row in rows:
        # print(row)
        # 获取整行数据，返回list
        line = [col.value for col in row]
        #第一行是标题
        if 0 == index:
            for i in range(len(line)):
                title.append(line[i])
                # print('title=', line[i])
        else:
            map={}
            # print('title=',title,title[0],title[1])
            for i in range(len(line)):
                # print('title[i]=',title[i])
                map[title[i]]=line[i]
            listData.append(map)
                # print('value=', line)
        index = index + 1
    data=json.dumps(listData,ensure_ascii=False)
    path=config.base_dirs+'\\其他\\基础评估\\omo_stat_groupname.json'
    with open(path, 'w', encoding="utf-8") as f:
        f.write(data)
    print('组=',data)
    print('---------------------------------------------')
    return listData

#解析题
def jiexiti(sheet):
    # print('sheet名称=', sheet)
    # print('根据坐标获取=',sheet['A1'].value,sheet['B1'].value)
    # print('根据坐标获取=', sheet['A2'].value, sheet['B2'].value)

    rows = sheet.rows
    # print(rows)
    title = []
    listData=[]
    index = 0
    # 迭代所有的行
    for row in rows:
        # print(row)
        # 获取整行数据，返回list
        line = [col.value for col in row]
        #第一行是标题
        if 0 == index:
            for i in range(len(line)):
                title.append(line[i])
                # print('title=', line[i])
        else:
            map={}
            # print('title=',title,title[0],title[1])
            for i in range(len(line)):
                # print('title[i]=',title[i])
                map[title[i]]=line[i]
            listData.append(map)
                # print('value=', line)
        index = index + 1

    data = json.dumps(listData, ensure_ascii=False)
    path = config.base_dirs + '\\其他\\基础评估\\omo_stat_question.json'
    with open(path, 'w', encoding="utf-8") as f:
        f.write(data)
    print('题=',data)
    print('---------------------------------------------')
    return listData

#解析选择项
def xzx(sheet):
    # print('sheet名称=', sheet)
    # print('根据坐标获取=',sheet['A1'].value,sheet['B1'].value)
    # print('根据坐标获取=', sheet['A2'].value, sheet['B2'].value)

    rows = sheet.rows
    # print(rows)
    title = []
    listData=[]
    index = 0
    # 迭代所有的行
    for row in rows:
        # print(row)
        # 获取整行数据，返回list
        line = [col.value for col in row]
        #第一行是标题
        if 0 == index:
            for i in range(len(line)):
                title.append(line[i])
                # print('title=', line[i])
        else:
            map={}
            # print('title=',title,title[0],title[1])
            for i in range(len(line)):
                # print('title[i]=',title[i])
                map[title[i]]=line[i]
            listData.append(map)
                # print('value=', line)
        index = index + 1
    data = json.dumps(listData, ensure_ascii=False)
    path = config.base_dirs + '\\其他\\基础评估\\omo_stat_question_options.json'
    with open(path, 'w', encoding="utf-8") as f:
        f.write(data)
    print('选择项=',data)
    print('---------------------------------------------')
    return listData

#组
def zufun(sheets):
    zuArr = fenzu(sheets[0])
    tiArr = jiexiti(sheets[1])
    xzxArr = xzx(sheets[2])
    # xzxfun(1, xzxArr)
    for item in zuArr:
        #获取题
        item['item']=tifun(item['id'],tiArr)
        print('----',item['item'])
        #获取选择项 {'question_id': 5, 'option_name': 'B. 没有', 'option_score': '0分'}
        # for item2 in item['item']:
        #     item2['item']=xzxfun(item2['id'],xzxArr)


    print('zuArr=',json.dumps(zuArr))

#题
def tifun(group_id,tiArr):
    for item in tiArr:
        if group_id==item['group_id']:
            return item


#选择项
def xzxfun(question_id,xzxArr):
    for item in xzxArr:
        print('===',item)
        if question_id==item['question_id']:
            return item

if __name__ == '__main__':
    path=config.base_dirs+'\\其他\\基础评估\\excel\\基础评估-初筛-表.xlsm'
    print(path)
    # 加载excel文件
    workbook = load_workbook(path)
    # 获取所有sheet的名称
    sheets = workbook.worksheets
    print('sheet文件=',sheets)
    # zu=fenzu(sheets[0])
    # ti=jiexiti(sheets[1])
    # xzx(sheets[2])
    # for sheet in sheets:
    #     sheetFun(sheet)
    zufun(sheets)







