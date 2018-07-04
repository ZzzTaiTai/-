import random
import string
import pymysql
def Generate_activation_code(number,length):
    #创建一个字典
    result={}
    #转换为列表
    source=list(string.ascii_letters)
    #index 从0开始到9
    for index in range(0,10):
        #在source列表添加转化为字符串的index
        source.append(str(index))
    while len(result) < number:
        key=''
        #index 从0开始到激活码长度
        for index in range(length):
            #每循环一次从source随机取出一个元素，添加在key上
            key+=random.choice(source)
        if key in result:
            pass
        else:
            result[key]=2
    for key in result:
        print (key)
    return result

def save_Mysql(result):
    try:
        #打开数据库连接
        conn=pymysql.connect(host="127.0.0.1",user="root",passwd="a74108520",db="mysql")
        #用cursor()方法创建一个游标对象cur
        cur=conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            #使用execute()方法执行SQL语句，如果不存在activation_code，则创建数据库
            cur.execute('CREATE DATABASE IF NOT EXISTS activation_code')
            #使用activation_code数据库
            cur.execute('USE activation_code')
            #新建code表，id整数非空使用AUTO_INCREMENT自增加每次加1，code字符串（32字节）非空
            #PRIMARY KEY 约束唯一标识数据库表中的每条记录，设置id 为主键
            cur.execute('''CREATE TABLE IF NOT EXISTS code(
                           id INT NOT NULL AUTO_INCREMENT,
                           code VARCHAR(32)NOT NULL,
                           PRIMARY KEY(id) 
                        )''')
            #code在result字典循环
            for code in result:
                #插入code表的code字段的值
                cur.execute('INSERT INTO code(code)VALUES(%s)',(code))
                #提交到数据库执行
                cur.connection.commit()
        except BaseException as e:
            print(e)
    #无论如何都会执行
    finally:
        cur.close()
        conn.close()


if __name__=="__main__":
    save_Mysql(Generate_activation_code(200,12))

