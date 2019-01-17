import time #通过小甲鱼的代码使用time.ctime()方法显示时间更方便
import pickle #储存二进制文件
import os #使用remove方法删除文件
class Mydes:
    def __init__(self, value = None, name = None):
        self.value = value
        self.name = name
        self.path = 'C:\\Users\\vulcanten\\desktop\\%s.txt' % self.name #不同的属性保存在不同的文件里面
    def __get__(self, instance, owner):
        with open(self.path, 'ab') as f:
            pickle.dump('Variable <%s> has been read at Beijing Time <%s>, %s = %s\n' % (self.name, time.ctime(), self.name, str(self.value)), f) #注意self.value不能用%d格式化需要转换成字符串形式，否则传入的值是不同类型时就会出现报错
        return self.value

    def __set__(self, instance, value):
        self.value = value
        with open(self.path, 'ab') as f:
            pickle.dump('Variable <%s> has been set at Beijing Time <%s>, %s = %s\n' % (self.name, time.ctime(), self.name, str(self.value)), f)
        

    def __delete__(self, instance):
        with open(self.path, 'ab') as f:
            pickle.dump('Variable <%s> has been deleted at Beijing Time <%s>\n' % (self.name, time.ctime()), f)
        os.remove(self.path) #删除属性的时候就删除了属性文件
        del self.value

class T:
    x = Mydes(10, 'x')
    y = Mydes(8.8, 'y')
