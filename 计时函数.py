import time as t

class Mytimer:
    #初始化一些参数
    def __init__(self, function = 0, times = 10000):
        self.lasted = 0
        self.prompt = 'Haven\'t start the timer.' #当没有开始计时器是会提示的信息
        self.default_timer = t.perf_counter #设置一个默认的计时器
        self.begin = 0
        self.end = 0
        self.function= function #需要调用来计时的函数
        self.times = times #需要调用的次数
        
    def __str__(self): #直接调用实例化对象时返回的信息
        return self.prompt
    
    
    __repr__ = __str__ #直接返回信息或者用print()

    
    def __add__(self, other): #对实例化对象进行加法运算
        totallasted = self.lasted + other.lasted
        prompt = 'Totally run %0.2f second.' % totallasted
        return prompt

    def timing(self):
        if not self.function: #如果没有调用函数，而直接调用这个方法，会出现提示
            print('Please call a function first.')
        else:
            self.start() #计时开始
            for i in range (self.times): #调用函数的次数
                self.function() #被调用的函数，加上括号才能算是调用完整的函数
            self.stop() #停止计时，持续时间记录在self.lasted里面
            prompt = 'This function totally run %0.2f second.' % self.lasted
            return prompt
            
        
    def set_timer(self): #设置计时器
        while 1:
            timer = input('Input the timer name: 1. process_timer 2.perf_counter.(1/2)')#做出选择
            if timer == '1':
                self.default_timer = t.process_time #调用方法不加括号相当于一个变量
                break
            elif timer == '2':
                self.default_timer = t.perf_counter
                break
            else:
                print('Input error, please input again.')

        
    def start(self): #开始计时
        self.begin = self.default_timer() #调用方法加括号得到函数的返回值
        print(self.begin)
        self.prompt = 'Please call stop() to stop the timer.' #如果只是调用开始，就直接调用实例化对象时，返回的信息
        print('Start the timer.')

    def stop(self):#停止计时
        if not self.begin: #如果计时器没有开始
            print('Please call the start() to start the timer.')
        else:
            self.end = self.default_timer()#调用方法加括号得到函数的返回值
            print(self.end)
            self._calt() #调用程序内部方法对持续的时间进行计算
            print('Stop the timer.')
    
    def _calt(self):
        self.lasted = self.end - self.begin
        self.prompt = 'Totally run %0.2f second.' % self.lasted
        
        self.begin = 0 #计算完后就再次归零，这样停止了之后只有再次调用开始，才能调用停止
        self.end = 0

        
