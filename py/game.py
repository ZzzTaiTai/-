from random import randint

name=input('please Input your name:')

f=open('di.txt','r')
lines=f.readlines()
f.close()

scores={}
for i in lines:
    s=i.split()
    print(s)
    scores[s[0]]=s[1:]
score=scores.get(name)
if score is None:
    score=[0,0,0]

#game_times游戏次数  min_times最快猜出的轮数  total_times总轮数 avg_times 平均轮数
game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])
if game_times > 0:
    avg_times=float(total_times/game_times)
else:
    avg_times=0
print("**********猜数游戏(1-100)*********")  
print("%s,你已经玩了%d次,最快%d轮猜出答案,平均%.2f轮猜出答案"%(
    name,game_times,min_times,avg_times))
#轮数

num=randint(1,100)
number =0
print ('1-99你觉得是多少?')

bingo=False
while bingo== False:
    number+=1
    you=int(input())
    if you> num:
        print ("大了一点")
    if you<num:
        print ("小了一点")
    if you==num:
        print ("Bingo")
        bingo=True


        
if game_times==0 or number<min_times:
    min_times=number
total_times+=number
game_times+=1

scores[name]=[str(game_times),str(min_times),str(total_times)]
result=''
for n in scores:
    line=n+' '+' '.join(scores[n])+'\n'
    print(line)
    result+=line
f=open('di.txt','w')
f.write(result)
f.close()
