import redis_test
obj=redis_test.RedisHelper()
data=obj.subscribe('fm110.1')
print('等待中')
print(data.parse_response())
