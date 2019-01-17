'''次程序是定制一个列表，并实现一些原生态的功能，并记录每个索引值被访问的次数.'''
class List:
    def __init__(self, *values): #这里允许用户传入任意个参数，作为列表的元素
        self.values = list(values) #把元组转化为列表
        self.count = {}.fromkeys([x for x in range(len(self.values))], 0) #使用字典的fromkeys构成列表的索引值为键，索引值使用的次数为值的字典，初始值为0

    def __len__(self):
        return len(self.values) #返回列表的长度

    def __getitem__(self, key):
        if key not in range(len(self.values)): #如果索引值超出范围
            raise IndexError('Index is out of range')
        self.count[key] += 1 #被引用一次就会在索引值的值加1
        return self.values[key]#返回列表中索引值的值

    def __setitem__(self, key, value):
        self.values[key] = value
        
    
    def __delitem__(self, key):
        del self.values[key]
        for x in range(key, len(self.count)-1):#删除一个元素后，总长度减一
            self.count[x] = self.count[x+1] #原来字典的value从key位置后等于后一个位置的键值
        self.count.popitem()#原字典的最后一个键被多出，需要删除。
        
       

    def __reversed__(self):
        list1 = []
        for i in range(len(self.values)-1, -1, -1): #列表倒置，按照序列号从最后到0迭代出列表的元素并写入新的列表，实现倒置。
            list1.append(self.values[i])
        self.values = list1
        y = list(self.count.values()) #同理记录访问次数的字典也需要倒置。
        y.reverse() #先导出字典的所有键值，再倒置，然后迭代如新的字典中。
        for x in range(len(self.count)):
            self.count[x] = y[x]

    def newappend(self, value): #在末尾加入一个元素，实际上等于在原列表加上这个元素组成的列表
        self.values = self.values + [value]
        self.count[len(self.count)] = 0 #在末尾加入一对键

    def newpop(self): #弹出最后一个元素
        self.maxindex = len(self.values) - 1
        print(self.values[self.maxindex])
        del self.values[self.maxindex]#删除最后一个元素
        self.count.popitem() #弹出字典的最后一对键
        
        

    def newremove(self, value):#删除从左至右第一次出现的一个值
        for i in range(len(self.values)):
            if self.values[i] == value:#找到这个值的序列号
                del self.values[i]
                for x in range(i, len(self.count)-1):#同上面__delitem__删除序列号的方法
                    self.count[x] = self.count[x+1]
                self.count.popitem()
                break #删除元素后立即停止循环
       
            
    def newinsert(self, key, value):#在列表中插入一个元素
        self.values = self.values[ : key] + [value] + self.values[key : ]#通过切片实现插入
        listvalues = list(self.count.values())#在字典键值组成的列表中
        listvalues.insert(key, 0)#插入对应key的元素0
        for x in range(len(listvalues)): #在通过迭代组成一个新的字典来实现插入
            self.count[x] = listvalues[x]
        
        
    def newclear(self):#清空
        self.values = []
        self.count  = {}

    def newreverse(self):#功能同__reversed__
        list1 = []
        for i in range(len(self.values)-1, -1, -1):
            list1.append(self.values[i])
        self.values = list1
        y = list(self.count.values())
        y.reverse()
        for x in range(len(self.count)):
            self.count[x] = y[x]

    def newextend(self, iterable):#在列表末尾加入多个元素，也就是加上多个元素组成的列表
        try: 
            for i in iterable: #判断是否是容器，否则会报错
                pass
            for x in range(len(iterable)):#容器里有几个元素，就在末尾添加几个item,字典的长度始终比最大的序列号多一
                self.count[len(self.count)] = 0
            self.values = self.values + list(iterable)
        except TypeError:
            print('%s is not iterable.' % str(iterable))       
        
     def counter(self, index):
         return self.count[index]
         

'''总结 1 list(string)的结果是每个字符串的字符组成列表，如果需要把
        整个字符串当作一个元素用[string]
        2 定义类时，要让所有的类变量在__init__定义和赋值，如果类变量
        类的方法中定义和赋值，如果这个方法没有被调用的话，这个
        类变量就不能使用
        3 在可变对象比如列表在进行自身操作时，比如添加，删除元素时，
        列表本身的id没有发生变化，他还是那个他，只是多吃了点肉，喝了
        水而已。所以python不会返回他的值，我们也不能对他进行另外的
        赋值操作。list1 = list1.append(self.values[i]) 像这样是不正确的。
        4 容器中的最后一个元素索引值是-1,倒数第二个是-2
        5 super()就是主体，可以进行计算赋值等。如：key = super().index(value)
        del self.count[key]，在此例中super()就是老师调用基类list来参与计算
        这样简化程序就不用再重写功能了。'''
