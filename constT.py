# 该模块用于让 Python 支持常量操作, 模块名constT.py
class Const:
    def __getattr__(self, name):#属性不存在时
        print('常量不存在')
    def __getattribute__(self, name): #返回已经存在的属性,在本例中可以不用这个属性
        return super().__getattribute__(name)
        
    def __setattr__(self, name, value):
        if name in self.__dict__: #如果在类的__dict__中存在的属性(常量)
            raise TypeError('常量无法改变！')
            
        if not name.isupper():#如果属性(常量)不是大写字母组成
            raise TypeError('常量名必须由大写字母组成！')

        self.__dict__[name] = value #类有一个__dict__的字典,键是类的属性名,键值是属性的值
        #初始化是一个空的字典本例，老师巧妙的利用了这个字典，第一可以判断属性是否已经
        #存在了，第二可以直接给属性赋值，可以避免死循环的错误，在小甲鱼教材第134，135
        #页有讲这个问题。

import sys
sys.modules[__name__] = Const() #在sys的模块中有一个记录python运行后所有导入的模块
#和模块对象组成的字典sys.modules,分别对应键和键值,__name__指对应的模块名
#在本例中我们把模块中的类的对象Const()替换了类对象, 使我们能够直接用模块调用
#类中的属性, 本例, 替换前我们要constT.Const.name来调用属性name,
#替代后，我们可以直接用constT.name来调用，因为我们调用模块名constT
#他的属性被Const()替换，所以等于同时调用了constT.Const, 这就让模块和
#类的属性直接联系起来。
