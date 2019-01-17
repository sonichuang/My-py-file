import os
import pickle

class T:
    saved = [] #保存以赋值的变量

    def __init__(self, name = None):
        self.name = name
        self.filename = self.name + '.pkl' #不同的属性保存在不同的文件里面

    def __get__(self, instance, owner):
        if self.name not in T.saved: #如果还没有赋值的属性会显示提示信息
            raise AttributeError("%s 属性还没有赋值！" % self.name) #在没有exception,fianlly的情况下当raise一个异常的时候就会停止运行下面的程序。这里相当于if....else...

        with open(self.filename, 'rb') as f:
            value = pickle.load(f) #因为是wb的方式写入文件，所以只有最后一次的赋值返回

        return value 

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f: #以wb的方式写入，会覆盖掉以前的值，所以只有最后一次赋值
            pickle.dump(value, f)
            T.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        T.saved.remove(self.name)
