

from  utils.dbUtil import DBMysql
from  utils import  strUtil
# 导入pymysql模块
import  pymysql
import  json
import  decimal
#如果报错，点击错误进行下载包
import requests
import  os
import  threading,time
import types
####################针对Decimal类型转换#######################################
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)
# 使用：
# data = json.dumps(数据, cls=DecimalEncoder,ensure_ascii=False)
# with open('omo_pe_question_path.json', 'w', encoding="utf-8") as f:
#     f.write(data)
###################################
#视频下载
def saveVideo(url):
    # url = 'https://img00.yuanxinkangfu.com/file/resource/201811/1543461141561.jpeg';

    pathRoot = 'D://com.yxkf.troops//'

    fileName = url[url.rfind('/') + 1:len(url)]
    print('资源文件名称=', fileName)

    # 获取文件夹
    fileDir = url[url.index('/resource/') + 1:url.rfind('/')]
    print('资源文件夹=', fileDir)
    if '2018' in fileDir or '20191' in fileDir:
        print('过滤老资源=',url)
        return

    # 创建文件夹
    pathDir = pathRoot + fileDir
    if not os.path.exists(pathDir):
        os.makedirs(pathDir)

    resourceName = pathRoot + fileDir + '//' + fileName
    print('本地资源路径=', resourceName)
    if not os.path.exists(resourceName):
        r = requests.get(url)
        with open(resourceName, "wb") as code:
            code.write(r.content)
            print(resourceName, '下载完成')
    else:
        print(resourceName, '存在')

#图片下载
#解析格式：
# url = 'https://img00.yuanxinkangfu.com/avthumb2/file/resource/20196/1561804143711.mp4';
# https://img00.yuanxinkangfu.com/file/resource/20191/1547024518714.png
# https://img00.yuanxinkangfu.com/file/resource/20194/1556499796276.png
def saveImg(url):
    # print('url=',url)

    # url = 'https://img00.yuanxinkangfu.com/avthumb2/file/resource/20196/1561804143711.mp4';
    # https://img00.yuanxinkangfu.com/file/resource/20191/1547024518714.png

    pathRoot = 'D://com.yxkf.troops//'

    fileName = url[url.rfind('/') + 1:len(url)]
    print('资源文件名称=', fileName)

    # 获取文件夹
    fileDir = url[url.index('/resource/') + 1:url.rfind('/')]
    print('资源文件夹=', fileDir)
    if '2018' in fileDir or '20191' in fileDir:
        print('过滤老资源=',url)
        return

    # 创建文件夹
    pathDir = pathRoot + fileDir
    if not os.path.exists(pathDir):
        os.makedirs(pathDir)

    resourceName = pathRoot + fileDir + '//' + fileName
    print('本地资源路径=', resourceName)
    if not os.path.exists(resourceName):
        r = requests.get(url)
        with open(resourceName, "wb") as code:
            code.write(r.content)
            print(resourceName, '下载完成')
    else:
        print(resourceName, '存在')

#解析omo_pe_question表的option字段的图片
#格式：https://img00.yuanxinkangfu.com/file/resource/20194/1556499796276.png
# def saveImg_omo_pe_question(url):
#     # print('url=',url)
#
#
#     pathRoot = 'C://com.yxkf.troops//'
#
#     fileName = url[url.rfind('/') + 1:len(url)]
#     print('资源文件名称=', fileName)
#
#     # 获取文件夹
#     fileDir = url[url.index('/resource/') + 1:url.rfind('/')]
#     print('资源文件夹=', fileDir)
#
#     # 创建文件夹
#     pathDir = pathRoot + fileDir
#     if not os.path.exists(pathDir):
#         os.makedirs(pathDir)
#
#     resourceName = pathRoot + fileDir + '//' + fileName
#     print('本地资源路径=', resourceName)
#     if not os.path.exists(resourceName):
#         r = requests.get(url)
#         with open(resourceName, "wb") as code:
#             code.write(r.content)
#             print(resourceName, '下载完成')
#     else:
#         print(resourceName, '存在')
###########下载视频和图片#################################
def downloadVideo(tableName):
    db = pymysql.connect(host='rm-8vb4r23m73kb7kty66o.mysql.zhangbei.rds.aliyuncs.com',
                         user='omo_military',
                         password='Omo_military123$',
                         database='omo_military',
                         charset='utf8', port=3306)
    cur = db.cursor()
    results = []

    try:
        # tableName
        # 'select * from omo_resource;'
        sql='select * from '+tableName+';';
        # 执行sql语句
        cur.execute(sql)
        # 获取查询的所有记录
        results = cur.fetchall()


        # 遍历结果
        for row in results:
            # print(row)
            if 'omo_resource'==tableName:
                url_video = row[7]
                url_img = row[11]
                url_img_content=row[10]
                print(url_img)
                if None != url_video and '' != url_video and url_video[-4:] == '.mp4' and len(url_video) > 0:
                    # print('mp4url=', url_video)
                    saveVideo(url_video)
                if None != url_img and '' != url_img and (url_img[-5:] == '.jpeg' or url_img[-4:] == '.png') and len(url_img) > 0:
                    saveImg(url_img)
                if 'http' in  url_img_content:
                    arr = json.loads(url_img_content)
                    for item in arr:
                        print('omo_resource表content',item['url'])
                        saveImg(item['url'])
                    pass

            elif 'omo_pe_cate'==tableName:
                url_img = row[3]
                print(url_img)
                if None != url_img and '' != url_img and (url_img[-5:] == '.jpeg' or url_img[-4:] == '.png') and len(url_img) > 0:
                    # print(url_img)
                    saveImg(url_img)
                pass
            elif 'omo_pe_question'==tableName:
                print(row)
                print('------------------')
                pass

    except Exception as e:
        print('错误 url=',url_video,',size=',len(url_video))
        raise e
    # finally:
        # db_sqlalchemy.close()  # 关闭连接
###########################################################
###########下载视频和图片-使用dbUtil工具下载#################################
def downloadVideo_dbUtil(sqlstr,tableName):
    try:
        results = DBMysql.findMulti(sqlstr)
        # print(results)
        if 'omo_pe_question'==tableName:
            for map in results:
                print('数据表id=', map['id'])
                _str=str(map['options'])
                print('options=',_str)
                if '['==_str[0:1]:
                    print('type(options)=',type(map['options']))
                    for item in strUtil.strToList(map['options']):
                        if ('value'  in item.keys())==False:
                            continue

                        url=item['value']
                        #判断数据类型
                        if  isinstance(url, str):
                            b = 'https' in url
                            if True==b:
                                print('url=', url)
                                saveImg(url)
    except Exception as e:
        print('错误 url=',e)
        raise e
    # finally:
        # db_sqlalchemy.close()  # 关闭连接
###########################################################
if __name__ == "__main__":
    downloadVideo('omo_resource')
    downloadVideo('omo_pe_cate')
    #下载option字段的图片
    downloadVideo_dbUtil('select * FROM omo_pe_question','omo_pe_question')

    print('=========完成=========')



