class Movestr(str):#需要在实例化的时候输入字符串，继承了字符串
    def __lshift__(self, other):#self就是实例化后的对象，other就是需要位移的步数，在这里是左移
        a = list(self) #对象所指的字符串转化成每个字符的列表
        a.insert(other, '/') #在从左至右列表第other个索引值位置，及other + 1个位置插入一个'/',插入这个符号是为了后面以这个符号为分割点
        b = ''.join(a) #把列表元素按照从前到后组成一个字符串
        c = b.split('/', 2) #以'/'字符为分割线，把字符串分割成参数2个字符串组成的列表
        c.reverse()#把列表中的元素前后倒置
        d = ''.join(c)#再把倒置的元素组成一个新的字符串
        return d
    def __rshift__(self, other):
        e = list(self)
        e.insert(-other, '/')#从后往前
        f = ''.join(e)
        g = f.split('/', 2)
        g.reverse()
        h = ''.join(g)
        return h
