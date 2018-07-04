#-*-coding:utf-8-*- 
import re
import time
import pickle
import random
import urllib.request,time,_thread
from functools import reduce
import requests
from lxml import html

'''print("等待2秒")
time.sleep(2)
text="site sea sue 156228637sweet see (021)88776543sda  010-55667890 sdsadasd 02584453362sd 0571 66345673 sse ssee13689535227 loses. 13689535227"
a=re.findall(r"\(?\d{3,4}[),-]?\d{7,8}",text)
print (a)

test=['one two',321,True,1.1]
f=open('HELLoboy.txt','wb')
pickle.dump(test,f)
f.close()

f=open('HELLoboy.txt','rb')
a=pickle.load(f)
f.close()
print(a)

list_2=[i for i in range(1,101) if i%2 ==0 and i%3==0 and i%5==0]
print (list_2)

def ALL(a,b,c):
        print(a,b,c)

ALL(1,2,3)

sum = lambda a,b,c:a+b+c
print(sum(1,2,3))


lst_1=[1,2,3,4,5,6]
lst_2=[1,3,5,7,9,11]
lst_3=list(map(lambda x,y:x+y,lst_1,lst_2))
print(lst_3)


sum=0
for i in range(1,101):
        sum+=i
print(sum)



def get_content(i):
        id=1764796+i
        url='https://api.douban.com/v2/movie/subject/%d' % id
        d=urllib.request.urlopen(url).read()
        data.append(d)
        print(i,time.time()-time_start)
        print("data:"+len(data))

time_start=time.time()
data=[]
for i in range(10):
         print("request movie:",i)
         _thread.start_new_thread(get_content,(i,))
         
input('press ENTER to exit..\n')
print()




def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
        try:
                r = calc('100 + 200 + 345')
                print('100 + 200 + 345 =', r)
                r = calc('99 + 88 + 7.6')
                print('99 + 88 + 7.6 =', r)
        except:
                print("Error")

main()

'''

cookie={}
raw_cookies='Mi4xZWdNZEF3QUFBQUFBVUlLcDViaF9EQmNBQUFCaEFsVk5KN1ViV3dBMVJCdlRjUkhnRjdCSmRFaEZRdk9hSS1fX2Fn|1512990503|e0943691beeaa5ba2dcc9bc98693b5f7062d9cef'

for line in raw_cookies.split(';'):
        key,value=line.split("=",1)
        cookie[key]=value

page=requests.get('',cookies=cookie)
tree=html.fromstring(page.text)
intro_raw=tree.xpath('')







