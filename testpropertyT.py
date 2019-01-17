class Myproperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        print('here')
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner): #self 指Myproperty本身的实例, instance指C的实例化对象c，owner指 C
        print('2')
        return self.fget(instance) #调用下面class C的getting()
    def __set__(self, instance, value):
        print('3')
        self.fset(instance, value) #调用下面class C的setting()
    def __delete__(self, instance):
        self.fdel(instance) #调用下面class deleting()

class C:
    def __init__(self):
        print('init')
        self._x = None
    def getting(self):
        print('getting')
        return self._x
    def setting(self, value):
        print('setting')
        self._x = value
    def deleting(self):
        print('deleting')
        del self._x
    t = Myproperty(getting, setting, deleting) #实例化会先调用Myproperty的__init__()，打印出here

        
c = C() #C实例化后会调用C的__init__ 会打印出‘init'
c.t #先调用Myproperty的__get__打印2 再调用C的getting，打印getting, 返回None
c.t = 1 #先调用Myoey的__set__打印3， 再调用C的setting, 打印setting, 给c._x赋值为1


