'''from random import choice
score=[0,0]
direction=['左','中','右']

def football():
    print ("——你倒是踢，踢进算我输——")
    print("——左，中，右选择一边射——")
    shoot=input()
    print("你已向"+shoot+"射击")
    cpu=choice(direction)
    print("守门员扑向了"+cpu)
    if shoot!=cpu:
        print("nice，这都能进了!")
        score[0]+=1
    else:
        print("没进,菜鸡")
        score[1]+=1
    print("%d(玩家得分)--%d(电脑得分)" %(score[0],score[1]))

    print ("——你倒是守，守到算我输——")
    print("——左，中，右选择一边守——")
    shoot=input()
    print("你已向"+shoot+"守")
    cpu=choice(direction)
    print("守门员踢向了"+cpu)
    if shoot==cpu:
        print("nice，这都守住了!")
        score[0]+=1
    else:
        print("没守住,菜鸡")
        score[1]+=1
    print("%d(玩家得分)--%d(电脑得分)" %(score[0],score[1]))
    
for i in range(3):
    print("————第%d回合————"%(i+1))
    football()

while(score[0]==score[1]):
    i+=1
    print("————第%d回合————"%(i+1))
    football()

if score[0]>score[1]:
    print("奇迹，你居然能赢")
else:
    print("辣鸡，你输了")
'''

#从HELLoboy.txt读出内容，保存至di.txt。
'''
f=open('HELLoboy.txt','r')
atxt=f.read()
print(atxt)
f.close()
a=open('di.txt','w')
a.write(atxt)
a.close()
'''
#从控制台输入一些内容，保存至di.txt。
'''
print("请输入些什么东西")
ditxt=input()
di=open('di.txt','w')
di.write(ditxt)
di.close()
'''
#异常处理，有错误则执行except
'''
try:
    f=open('di.txt')
    lines=f.readlines()
    print("打开成功")
    f.close()
except:
    print("打开失败")
    print("null")

results=[]
for line in lines:
    data=line.split()
    print(data)
    sum=0
    for score in data[1:]:
        sum+=int(score)
    result='%s\t:%d\n'%(data[0],sum)
    results.append(result)
copy=open('result.txt','w')
copy.writelines(results)
copy.close()
'''
#字典基本格式是（key是键，value是值）：d = {key1 : value1, key2 : value2 }
'''
score={
    '泰':100,
    '庆':98,
    'TAI':95
    }
print(score['TAI'])
score['TAI']=96
score['QING']=95
score['ZZ']=95
for name in score:
    print (name,score[name])
del score['ZZ']
'''
#引用模块
'''
import math
print (math.pi)

#from math import pi as math_pi自定义名
from math import pi
print(pi)

'''




'''
name='Tai'
tedian='shuai'
print('%s is very %s'%(name,tedian))
print ('Hello'+'1')
x=-1
y=-1
def nice(Hello,Hello1):
    print (Hello+Hello1)
#nice(-1,1)
if x>=0:
    if y>=0:
        print ("1")
    else:
        print ("4")
else:
    if y<0:
        print ("3")
    else:
        print ("2")
I=['666','shuai','gg','6123']
I[1]='Tai666'
I.append("Tai")
I.append("Taione")
del I[2]
for i in I:
    print (i)
'''
