from datetime import datetime #datetime模块中的datetime类
dt = datetime.now #datetime类的方法, 在这里是变量转移，到后面需要调用时才加括号调用
path = 'C:\\Users\\vulcanten\\desktop\\record.txt'
with open(path, 'w') as f: #安全打开文件的方式，在这里是为了让文件清空
    pass

class Mydes:
    def __init__(self, value = None, name = None):
        self.value = value
        self.name = name

    def __get__(self, instance, owner):
        timestr = dt().strftime('%c') #加括号调用时间并格式化详见 https://fishc.com.cn/forum.php?mod=viewthread&tid=51725&extra=page%3D1%26filter%3Dtypeid%26typeid%3D403
        with open(path, 'a') as f: #在文件的末尾写入
            f.write('Variable <%s> has been read at Beijing Time <%s>, %s = %s\n' % (self.name, timestr, self.name, str(self.value))) #注意self.value不能用%d格式化需要转换成字符串形式，否则传入的值是不同类型时就会出现报错
        return self.value

    def __set__(self, instance, value):
        self.value = value
        timestr = dt().strftime('%c')
        with open(path, 'a') as f:
            f.write('Variable <%s> has been set at Beijing Time <%s>, %s = %s\n' % (self.name, timestr, self.name, str(self.value)))
        

    def __delete__(self, instance):
        timestr = dt().strftime('%c')
        with open(path, 'a') as f:
            f.write('Variable <%s> has been deleted at Beijing Time <%s>\n' % (self.name, timestr))
        del self.value

