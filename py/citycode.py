#-*- coding:utf-8 -*-
from urllib.request import urlopen

url1='http://m.weather.com.cn/data3/city.xml'
content1=urlopen(url1).read()
provinces=content1.decode('utf-8').split(',')

result='city={\n'
url= 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code=p.split('|')[0]
    url2=url%p_code
    content2=urlopen(url2).read()
    cities=content2.decode('utf-8').split(',')
    #print(cities)
    for c in cities[:100]:
        c_code=c.split('|')[0]
        url3=url%c_code
        content3=urlopen(url3).read()
        districts=content3.decode('utf-8').split(',')
        #print(districts)
        for d in districts:
            d_pair=d.split('|')
            d_code=d_pair[0]
            name=d_pair[1]
            url4=url%d_code
            content4=urlopen(url4).read()
            code=content4.decode('utf-8').split('|')[0]
            print (name+':'+code)
            line="%s:%s\n"%(name,code)
            result+=line
result+='}'
f=open('city_code.py','w')
f.write(result)
f.close()
