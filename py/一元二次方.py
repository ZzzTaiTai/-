import math
print("请输入a,b,c的数值")
a=int(input())
b=int(input())
c=int(input())
try:
    num=(-b+math.sqrt(pow(b,2)-4*a*c))/2*a
    print(num)
except:
    print("方程无解")
   
