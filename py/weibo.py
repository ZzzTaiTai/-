import re
import string
import sys
import reload
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import shutil
import time
from lxml import etree
'''
cookie:_T_WM=68f2d179234a5296d88442ebc1b49235; login=ec1b2ebb0879ca371fdf54d7c71fe5fa; ALF=1528427120; SCF=ArgUsUIBmlKCYhhKef65YzFM2gSrbpZsDe2QsThKauvqzrCUelp6ttvf6lKsC0goi-MMXMR4GjR5ZmfkLh41hSQ.; SUB=_2A2539hUqDeRhGeRL71UV9y_OzjyIHXVVGLtirDV6PUJbktANLUPgkW1NUyMhnj5nG06dUH8_Xr73gyAlaWyckJs8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFi_r3QjifRJ.aPPlF_nGek5JpX5K-hUgL.FozfShMXS02ESK52dJLoI7yIwrDAPfxyIBtt; SUHB=0wnEKz4fE0ZCVC; SSOLoginState=1525835130
'''

reload(sys)
sys.setdefaultencoding('utf-8')
#爬取当前微博用户ID
user_id='2743636135'
cookie={"Cookie":"_T_WM=68f2d179234a5296d88442ebc1b49235; login=ec1b2ebb0879ca371fdf54d7c71fe5fa; ALF=1528427120; SCF=ArgUsUIBmlKCYhhKef65YzFM2gSrbpZsDe2QsThKauvqzrCUelp6ttvf6lKsC0goi-MMXMR4GjR5ZmfkLh41hSQ.; SUB=_2A2539hUqDeRhGeRL71UV9y_OzjyIHXVVGLtirDV6PUJbktANLUPgkW1NUyMhnj5nG06dUH8_Xr73gyAlaWyckJs8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFi_r3QjifRJ.aPPlF_nGek5JpX5K-hUgL.FozfShMXS02ESK52dJLoI7yIwrDAPfxyIBtt; SUHB=0wnEKz4fE0ZCVC; SSOLoginState=1525835130"}
url='http://weibo.cn/u/%d?filter=1&page=1'%user_id
html= requests.get(url,cookie=cookie).content
print('user_id和cookie读入成功')
selector=etree.HTML(html)
#获取当前微博总共的页数
pageNum=(int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])

result=""
urllist_get=set()
word_count=1
image_count=1

print('ready')
print(pageNum)
#刷新输出
#sys.stdout.flush()

times = 5
#58/5=11.6
one_step=pageNum/times
#step在0到times循环

for step in range(times):
    if step< times-1:
        i= step * one_step+1
        j=(step+1)*one_step+1
    else:
        i=step * one_step+1
        j=pageNum+1
    for page in range(i,j):
        #获取lxml页面
        try:
            url='http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page)
            lxml=requests.get(url,cookies=cookie).content
            selector=etree.HMTL(lxml)
            content=selector.xpath('//span[@class="ctt"]')
            for each in content:
                text =each.xpath('string(.)')
                if word_count >= 3:
                    text ="%d:"%(word_count-2)+text+"\n"
                else:
                    text=text+"\n\n"
                result=result+text
                word_count+=1
            print (page,'word ok')
            soup=BeautifulSoup(lxml,"lxml")
            urlist=soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/oripic',re.I))
            urllist2=soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/picAll',re.I))
            for imgurl in urlist:
                #imgurl['href']



