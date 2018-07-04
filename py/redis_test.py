import redis
class RedisHelper:
    def __init__(self):
        self.__conn=redis.Redis(host="127.0.0.1",port=6379)
    def publish(self,msg,chan):
        self.__conn.publish(chan,msg)#在chan频道发布消息
        return True
    def subscribe(self,chan): #订阅接收
        pub=self.__conn.pubsub() #打开收音机
        pub.subscribe(chan) #订阅频道
        pub.parse_response() #等待消息
        return pub #开始接收



