#-*- coding:utf-8 -*-
import re
import requests

q=raw_input('请输入需要搜索的关键词（搜索引擎Bing）')
url='https://cn.bing.com/images/search?q='+q+'&qs=IM&form=QBILPG&sp=1&pq=xiaohuangr&sc=8-10&sk=&cvid=F0981A50C329494D8AF206CFD313E3DF'

bing_p=requests.get(url).text
bing_url=re.findall('http://.{1,100}.jpg|http://.{1,100}.png|http://.{1,100}.jpeg',bing_p,re.S)
i=0
for j in bing_url:
    print j
    try:
        b_p_url=requests.get(j,timeout=5)
    except requests.exceptions.ConnectionError:
        print '当前图片无法下载'
        continue
    string='photo\\'+str(i)+'.jpg'
    ct=open(string,'wb')
    ct.write(b_p_url.content)
    ct.close()
    i+=1