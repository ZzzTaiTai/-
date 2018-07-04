class Vehicle:
    # __init__方法初始化速度
    def __init__(self,speed):
       self.speed=speed
    def drive(self,distance):
        print('需要%f小时'%(distance/self.speed))
        #drive方法 路程distance除于速度求得时间 
class Bike(Vehicle):
    pass
class Car(Vehicle):
    # __init__ 方法初始化 速度 油耗fuel
    def __init__(self,speed,fuel):
        # __init__ 方法调用Vehicle初始化速度
        Vehicle.__init__(self,speed)
        self.fuel=fuel
    #drive方法 路程*每公里需要的油耗得出总油耗
    def drive(self,distance):
        #调用Vehicle的drive方法初始化
        Vehicle.drive(self,distance)
        print('需要%f的油'%(distance*self.fuel))
            

        
#need %f fuels need %f hour(s)
b = Bike(15.0)
c = Car(80.0, 0.012)
b.drive(100.0)
c.drive(100.0)
