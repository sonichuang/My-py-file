class Stack:
    def __init__(self, start=[]):#start是关键字参数，默认为空列表，当列表不为空是，里面的元素将被迭代被放入栈中
        self.stack = []
        for x in start: #这里迭代出关键字参数列表里面的元素
            self.push(x)

    def isEmpty(self): #如果self.stack为空即为False,则返回Tue
        return not self.stack
    
    def push(self, obj):#在列表末尾加入元素
        self.stack.append(obj)

    def pop(self):
        if not self.stack:#在Python中 None, False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False,所以当self.stack为空时，就会执行后面的语句。
            print('警告：栈为空！')
        else:
            return self.stack.pop()#从末尾弹出一个元素

    def top(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[-1]#后进先出原则，最后append的元素在末尾

    def bottom(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[0]#先进后出原则，最后先进的元素在头

