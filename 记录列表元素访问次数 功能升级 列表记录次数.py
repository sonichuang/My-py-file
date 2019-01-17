'''次程序是定制一个列表，并实现一些原生态的功能，并记录每个索引值被访问的次数.'''
class List:
    def __init__(self, *values): #这里允许用户传入任意个参数，作为列表的元素
        self.values = list(values) #把元组转化为列表
        self.count = [] #初始化时，生成一个列表，与self.values相对应序列号的元素为0；
        for x in range(len(self.values)):
            self.count.append(0)
            
    def __len__(self):
        return len(self.values) #返回列表的长度

    def __getitem__(self, key):
        if key not in range(len(self.values)): #如果索引值超出范围
            raise IndexError('Index is out of range')
        self.count[key] += 1 #被引用一次就会在索引值的值加1
        return self.values[key]#返回列表中索引值的值

    def __setitem__(self, key, value):
        self.values[key] = value
        self.count[key] += 1
    
    def __delitem__(self, key):
        del self.values[key]
        for x in range(key, len(self.count)-1):#删除一个元素后，总长度减一
            self.count[x] = self.count[x+1] #原来计数的列表的value从key位置后等于后一个位置的键值
        self.count.pop()#原列表的最后一个键被多出，需要删除。
        
    def __reversed__(self):
        list1 = []
        list2 = []
        for i in range(len(self.values)-1, -1, -1): #列表倒置，按照序列号从最后到0迭代出列表的元素并写入新的列表，实现倒置。
            list1.append(self.values[i])
        self.values = list1
        for x in range(len(self.count)-1, -1, -1):#同理计数的列表同样的操作
            list2 .append(self.count[x])
        self.count = list2

    def newappend(self, value): #在末尾加入一个元素，实际上等于在原列表加上这个元素组成的列表
        self.values = self.values + [value]
        self.count = self.count + [0] #在末尾加入一个元素0

    def newpop(self): #弹出最后一个元素
        self.maxindex = len(self.values) - 1
        print(self.values[self.maxindex])
        del self.values[self.maxindex]#删除最后一个元素
        del self.count[len(self.count)-1]#弹出计数列表的最后一个元素
        
    def newremove(self, value):#删除从左至右第一次出现的一个值
        for i in range(len(self.values)):
            if self.values[i] == value:#找到这个值的序列号
                del self.values[i]
                for x in range(i, len(self.count)-1):#同上面__delitem__删除序列号的方法
                    self.count[x] = self.count[x+1]
                self.count.pop()
                break #删除元素后立即停止循环
       
            
    def newinsert(self, key, value):#在列表中插入一个元素
        self.values = self.values[ : key] + [value] + self.values[key : ]#通过切片实现插入
        self.count.insert(key, 0)#插入对应key的元素0
       
        
    def newclear(self):#清空
        self.values = []
        self.count  = {}

    def newreverse(self):#功能同__reversed__
        list1 = []
        list2 = []
        for i in range(len(self.values)-1, -1, -1):
            list1.append(self.values[i])
        self.values = list1
        for x in range(len(self.count)-1, -1, -1):#同理计数的列表同样的操作
            list2 .append(self.count[x])
        self.count = list2

    def newextend(self, iterable):#在列表末尾加入多个元素，也就是加上多个元素组成的列表
        try: 
            for i in iterable: #判断是否是容器，否则会报错
                pass
            for x in range(len(iterable)):#容器里有几个元素，就在末尾添加几个0,列表的长度始终比最大的序列号多一
                self.count += [0]
            self.values = self.values + list(iterable)
        except TypeError:
            print('%s is not iterable.' % str(iterable))       
        
    def counter(self, index):
        return self.count[index]
        


