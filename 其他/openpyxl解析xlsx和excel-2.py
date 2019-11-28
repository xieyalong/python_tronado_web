
from openpyxl import load_workbook

#解析没一个sheet
def sheetFun(s_name,workbook):
    i = 0
    print('sheet名称=', s_name)
    # 根据名字获取每个sheet文件 有报错 不用管
    sheet = workbook.get_sheet_by_name(s_name)
    # print(sheet)
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
        #第一行是标题
        if 0 == i:
            print('title=', line)
        else:
            print('value=', line)
        i = i + 1


if __name__ == '__main__':
    # 加载excel文件
    workbook = load_workbook(r'C:\test\1.xlsx')
    # 获取所有sheet的名称
    sheets = workbook.get_sheet_names()
    print('sheet文件=',sheets)
    for s_name in sheets:
        sheetFun(s_name,workbook)






