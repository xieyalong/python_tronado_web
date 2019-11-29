
from openpyxl import load_workbook

#解析没一个sheet
def sheetFun(sheet):
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
        #第一行是标题
        if 0 == i:
            print('title=', line)
        else:
            print('value=', line)
        i = i + 1


if __name__ == '__main__':
    # 加载excel文件
    workbook = load_workbook(r'C:\test\初筛表录入内容.xlsm')
    # 获取所有sheet的名称
    sheets = workbook.worksheets
    print('sheet文件=',sheets)
    for sheet in sheets:
        sheetFun(sheet)




# 角色编号 1=士兵，2=医务并，3=军，4=旅，5=营或团，6=连，7=排，8=班
# 这些时分秒 要写成 114100  001974  这样写
# 性别写成 1=男 2=女 0=未知
#pid：


