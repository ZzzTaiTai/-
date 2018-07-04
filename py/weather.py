from urllib.request import urlopen 
from city import city
import json

#
'''f=open('zhihu.html','wb+')
f.write(content)
f.close()'''


cityname=input('输入需要查询天气的城市\n')
citycode = city.get(cityname)
if citycode:
    try:
        url=('http://www.weather.com.cn/data/cityinfo/%s.html'%citycode)
        content=urlopen(url).read()
#print(content.decode('utf-8'))
        #JSON编码的字符串转换回一个Python数据结构
        data=json.loads(content)        
        result=data['weatherinfo']
        str_temp=('%s\n%s～%s')%(
            result['weather'],
            result['temp1'],
            result['temp2']    
        )
        print(str_temp)
    except:
        print("查询失败")
else:
    print("没有查询到此城市")
