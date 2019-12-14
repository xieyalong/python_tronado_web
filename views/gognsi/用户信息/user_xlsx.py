#处理xlsx


from openpyxl import load_workbook
import  config
import  json

def xlsx(sheet):
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
        # print(line)

        #第一行是标题
        if 0 == index:
            i = 0
            for i in range(len(line)):
                title.append(line[i])
            # print('title=',title)
        else:
            i = 0
            map={}
            for i in range(len(line)):
                str_title=title[i]
                map[str_title]=line[i]
                # print(str_title,line[i])
            print('---------------------------------------------')
            print('map',map)
            listData.append(map)

        index = index + 1
    print('------------------listData---------------------------')
    print('listData=',listData)
    # print(listData)
    # data=json.dumps(listData,ensure_ascii=False)
    # print(data)
    # path=config.base_dirs+'\\其他\\基础评估\\omo_stat_groupname.json'
    # with open(path, 'w', encoding="utf-8") as f:
    #     f.write(data)
    # print('组=',data)
    print('---------------------------------------------')
    return listData


def dispose(listData):
    for item in listData:
        birthday = item['birthday']
        if None!=birthday:
            birthday=birthday.strftime('%Y-%m-%d')
            item['birthday']=birthday
            # print('birthday=',birthday)
        else:
            item['birthday']=''

        if '......'==item['parent_id'] or None ==item['parent_id']:
            item['parent_id'] = ''

        # if None == item['user_name']:
        #     item['user_name'] = ''
        #
        # if None == item['name']:
        #     item['name'] = ''
        # if None == item['name']:
        #     item['name'] = ''
        print('itme=',item)
    return  listData


def mian():
    path = config.base_dirs + '\\其他\\用户信息\\处理.xlsx'
    print(path)
    # 加载excel文件
    workbook = load_workbook(path)
    # 获取所有sheet的名称
    sheets = workbook.worksheets
    print('sheet文件=', sheets)
    return dispose(xlsx(sheets[0]))


if __name__ == '__main__':
    path=config.base_dirs+'\\其他\\用户信息\\处理.xlsx'
    print(path)
    # 加载excel文件
    workbook = load_workbook(path)
    # 获取所有sheet的名称
    sheets = workbook.worksheets
    print('sheet文件=',sheets)
    dispose(xlsx(sheets[0]))
    # for sheet in sheets:
    #     xlsx(sheet)










