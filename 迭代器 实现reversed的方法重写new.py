'''要求写一个类实现reversed()的方法'''
class Myrev(str): #继承了str，所以他本是就是迭代器的功能
    def __new__(cls, string=''): #重写__new__方法
        if isinstance(string, str):
            string = string[::-1] #用字符串切片步长为-1的方法实现倒置
        return str.__new__(cls, string)

myrev = Myrev('FishC')
for x in myrev:
    print(x, end='')    

 
    
        

        
