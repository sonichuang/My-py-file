class F:
    def __init__(self, x = 0):
        self.x = x
    def __get__(self, instance, owner): #instance指T的实例化对象t
        return self.x
    def __set__(self, instance, value):
        self.x = float(value)    
class C:
    def __get__(self, instance, owner):#instance指T的实例化对象t
        return (instance.f - 32) / 1.8 
    def __set__(self, instance, value):
        instance.f = value * 1.8 + 32
class T:
    f = F() #运行程序时先实例化F
    c = C() #运行程序时先实例化C

t = T() #实例化T
t.f #调用F的__get__, 返回f.x的值为零
t.c #调用C的__get__, 返回(t.f -32) / 1.8, 即换算成摄氏度
t.f = 1 #调用F的 __set__，赋值给f.x
t.c #调用C的__get__, 返回(t.f -32) / 1.8, 即换算成摄氏度
t.c = 100 #调用C的__set__, 则会计算t.f = 100 * 1.8 + 32 换算成华氏度
t.f


