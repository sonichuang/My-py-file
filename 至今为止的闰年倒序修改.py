'''要求按照倒序打印至今的闰年'''
class Leapyears:
    def __init__(self, m = 2018):
        self.m = m
    def __iter__(self):
        return self
    
    def isleapyear(self, year):
        if (year%4 == 0 and year%100 != 0) or (year%400) == 0:
            return True
        else:
            return False
            
    def __next__(self):
        while not self.isleapyear(self.m):
            self.m -= 1
        self.year = self.m
        self.m -= 1
        if not self.m: #如果self.m等于0就停止迭代
            raise StopIteration
        return self.year #返回每一个值

leapyears = Leapyears()
for x in leapyears:
    if x >= 2000: #要求打印出2000后到至今
        print(x)
    else:
        break
        
