import datetime

date=datetime.datetime(1992, 12, 1, 0, 0)
#返回字符串
_str=date.strftime('%Y-%m-%d')
#输出 1992-12-01
print(_str)
print(type(_str))

# str='datetime.datetime(1992, 12, 1, 0, 0)'
# str=str[str.index('('),str.la(')')]
# print(str)