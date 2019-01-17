'''要求按照倒序打印至今的闰年'''
class Leapyears:
    def __init__(self, m = 2018):
        self.m = m
    def __iter__(self):
        return self
    def __next__(self):
        self.x = (self.m//4)*4 #计算出至今最近的一年
        self.m -= 4 #叠减4, 计算出每个闰年
        if not self.x: #如果self.x等于0就停止迭代
            raise StopIteration
        return self.x #返回每一个值

leapyears = Leapyears()
for x in leapyears:
    if x >= 2000: #要求打印出2000后到至今
        print(x)
        
