

import types
import  json
url='[{"url":"https://img00.yuanxinkangfu.com/file/resource/20189/1536746229387.jpeg","des":"定位不清"},{"url":"http://img00.sun-hc.com/file/resource/20186/1529574210070.jpeg","des":"注意事项：在治疗过程中，应及时询问用户的适应程度，如出现过烫，可再垫层毛巾，注意防止烫伤。"}]'

arr=json.loads(url)
for item in arr:
    print(item['url'])









