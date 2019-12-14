#处理xlsx


from openpyxl import load_workbook
import  config
import  json

#解析分组
def xlsx(sheet):
    i = 0
    # print('sheet名称=', sheet)
    # print('根据坐标获取=',sheet['A1'].value,sheet['B1'].value)
    # print('根据坐标获取=', sheet['A2'].value, sheet['B2'].value)

    rows = sheet.rows
    # print(rows)
    i = 0
    # 迭代所有的行
    for row in rows:
        # print(row)
        # 获取整行数据，返回list
        line = [col.value for col in row]
        print(line)
        #第一行是标题
        if 0 == i:
            print('title=', line)
        else:
            print('value=', line)
        i = i + 1


if __name__ == '__main__':
    path=config.base_dirs+'\\其他\\用户信息\\用户数据.xlsx'
    print(path)
    # 加载excel文件
    workbook = load_workbook(path)
    # 获取所有sheet的名称
    sheets = workbook.worksheets
    print('sheet文件=',sheets)
    # zu=fenzu(sheets[0])
    # ti=jiexiti(sheets[1])
    # xzx(sheets[2])
    for sheet in sheets:
        xlsx(sheet)










