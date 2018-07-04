#-*-coding:utf-8 -*-
import re
import requests


def Baidu(word):
    '''word=raw_input('请输入想要下载的的关键词')'''

    url ='http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1460997499750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word='+word+''


    rq=requests.get(url).text
    rq.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
    qc_url=re.findall('"objURL":"(.*?)",',rq,re.S)


    i=0
    for j in qc_url:
        print j
        try:
            qc=requests.get(j,timeout=5)
        except requests.exceptions.ConnectionError:
            print '当前图片无法下载'
            continue
        string='photo\\'+str(i)+'.jpg'
        cd=open(string,'wb')
        cd.write(qc.content)
        cd.close()
        i+=1

def Bing(bing):
    q=bing
    url = 'https://cn.bing.com/images/search?q=' + q + '&qs=IM&form=QBILPG&sp=1&pq=xiaohuangr&sc=8-10&sk=&cvid=F0981A50C329494D8AF206CFD313E3DF'

    bing_p = requests.get(url).text
    bing_url = re.findall('http://.{1,100}.jpg|http://.{1,100}.png|http://.{1,100}.jpeg', bing_p, re.S)
    i = 0
    for j in bing_url:
        print j
        try:
            b_p_url = requests.get(j, timeout=5)
        except requests.exceptions.ConnectionError:
            print '当前图片无法下载'
            continue
        string = 'photo\\' + str(i) + '.jpg'
        ct = open(string, 'wb')
        ct.write(b_p_url.content)
        ct.close()
        i += 1

xzyq=raw_input('请输入搜索引擎（BaiDu，Bing）')
print xzyq
if(xzyq=='BaiDu'):
    a=raw_input('请输入搜索的关键词')
    Baidu(a)
if(xzyq=='Bing'):
    b= raw_input('请输入搜索的关键词')
    Bing(b)
else:
    print'请选择搜索引擎'