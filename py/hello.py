def isTrue(num1,num2):
    if num1>num2:
        print('too big')
        return False
    if num1<num2:
        print('too small')
        return False
    if num1==num2:
        print ('good boy')
        return True
    
from random import randint
num=randint(1,100)
Bingo=False
while Bingo==False:
    print("请输入数字")
    you=int(input())
    Bingo=isTrue(you,num)
