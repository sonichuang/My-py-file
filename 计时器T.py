import time as t
class Mytimer:
    #初始化一些参数
    def __init__(self):
        self.unit = [' year ', ' month ', ' day ', ' hour ', ' minute ', ' second ']
        self.prompt = 'Haven\'t start the timer.' #当没有开始计时器是会提示的信息
        self.lasted = [] #通过列表的操作进行字符串拼接
        self.begin = 0
        self.end = 0
        
    def __str__(self): #直接调用实例化对象时返回的信息
        return self.prompt
    
    
    __repr__ = __str__ #直接返回信息或者用print()

    
    def __add__(self, other): #对实例化对象进行加法运算
        prompt = 'Total run '
        result = []
        for index in range (6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += str(result[index]) + self.unit[index]
        return prompt

        
    def start(self): #开始计时
        self.begin = t.localtime()
        self.prompt = 'Please call stop() to stop the timer.' #如果只是调用开始，就直接调用实例化对象时，返回的信息
        print('Start the timer.')

    def stop(self):#停止计时
        if not self.begin: #如果计时器没有开始
            print('Please call the start() to start the timer.')
        else:
            self.end = t.localtime()
            self._calt() #调用程序内部方法对持续的时间进行计算
            print('Stop the timer.')

    def _calt(self):
        self.lasted = []
        self.prompt = 'Totally run '
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index] ) #对localtime()返回的元组每一个索引值的元素进行计算
            if self.lasted[index]: #如果这个索引值的计算结果为零就不予显示
                self.prompt += str(self.lasted[index] ) + self.unit[index]#每一个索引值对应一个单位
        
        self.begin = 0 #计算完后就再次归零，这样停止了之后只有再次调用开始，才能调用停止
        self.end = 0

        
