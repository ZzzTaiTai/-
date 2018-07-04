import random
import string
import pymysql
import redis
#练习0001
#string.ascii_letters+string.digits
# 创建一个字典
#转换为列表
#index 从0开始到9
#在source列表添加转化为字符串的index
#index 从0开始到激活码长度
#每循环一次从source随机取出一个元素，添加在key上


def code(number,length):
    result={}
    source=list(string.ascii_letters+string.digits)
    while len(result)<number:
        key=''
        for index in range(length):
            key+=random.choice(source)
        if key in result:
            pass
        else:
            result[key]=2
    for key in result:
        print(key)
    return result
            #创立数据库
            #使用数据库
            #新建表格code 字段id 自动增长整数非空  code varchar32 非空 id为主键

def save_code_lx(result):
    try:
        conn=pymysql.connect(host='127.0.0.1',user='root',password='a74108520',db='mysql')
        cur=conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            cur.execute('drop database if exists b_code')
            cur.execute('create database if not exists b_code')
            cur.execute('use b_code')
            cur.execute('''create TABLE if not exists code(
                        id int not null auto_increment,
                        code varchar(32)not null,
                        primary key(id)
                        )''')
            for code in result:
                cur.execute('insert into code(code) values(%s)',(code))
                cur.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        conn.close()
        cur.close()
def save_redis(result,filepath):
    r=redis.Redis(host='localhost',port=6379)
    f=open(filepath,'w')
    end='---end---'
    for items in result:
        f.writelines(items+"\n")
        r.lpush('list2',items)
    r.lpush('list2',end)
    f.write(end)
    f.close()

if __name__=='__main__':
    save_code_lx(code(50,10))
    save_redis(code(2,15),r'C:\Users\lenovo\Desktop\one.txt')