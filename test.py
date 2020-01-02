

import types
url='https://img00.yuanxinkangfu.com/file/resource/20191/1547024518714.png';
fileName = url[url.rfind('/') + 1:len(url)]
print('资源文件名称=', fileName)

# 获取文件夹
fileDir = url[url.index('/resource/') + 1:url.rfind('/')]
print('资源文件夹=', fileDir)
print('2018' in fileDir or '20191' in fileDir)






