'''迭代器实现reversed()的功能,这个程序使用了普通迭代器的方法'''
class Myrev:
    def __init__(self, string=''):
        self.string = string
        self.x = 0
        
    def __iter__(self):
        return self

    def __next__(self): #在__next__中return必须在循环以外,并且返回一个特定的值
        self.x -=1 #叠加减等是比较常用的方法,这样才会返回一个特定的值
        if self.x < -len(self.string):#如果序列号用负值,第一个序列号为-len()
            raise StopIteration        
        y = self.string[self.x] #用负值实现从右到左依次出现每个元素
        return y

myrev = Myrev('FishC')
for x in myrev:
    print(x, end='')
    
        

        
