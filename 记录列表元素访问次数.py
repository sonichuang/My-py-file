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
