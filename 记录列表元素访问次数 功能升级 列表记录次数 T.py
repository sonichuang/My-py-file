'''老师的代码利用了继承list的方法，这样不用再重写那些列表的基本方法，
就只是实现计数的功能。'''
class CountList(list):
    def __init__(self, *args):#这里args是一个元组
        super().__init__(args)
        self.count = []#初始化与原列表对应序列号的元素为0
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)#super()就是让object类及list参与运算

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):#容器最后一个序列号从-1开始
        del self.count[key]
        return super().pop(key)

    def remove(self, value):#从这里看super()就相当于object一个主体，可以进行计算
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()
