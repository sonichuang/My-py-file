import datetime as dt

class LeapYear: 
    def __init__(self):
        self.now = dt.date.today().year #用datetime模块调出今年

    def isLeapYear(self, year): #类的内部函数判断是否是闰年，然后再返回True或者False
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False
        
    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now): #while 循环，直到是闰年返回True为止。
            '''注意类的内部函数需要用self.来调用'''
            self.now -= 1 #如果不是闰年，叠减1，直到内部函数返回True.

        temp = self.now #赋值给一个临时变量
        self.now -= 1 #再减一变成非闰年，进行下一次迭代
        '''这里可以加一段代码，让迭代器可以在一定的值停止raise StopIteration'''
        return temp
