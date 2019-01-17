import time as t  #这段代码是需要实现一个计时器的功能。
class Mytimer:
    def __init__(self): #初始化调用计时器开始的次数，没实例化一个对象就初始化为零
        self.countstart = 0
    def start(self):  #计时器开始
        print('Start the timer......')
        self.countstart += 1 #调用一次开始就会计数
        timestart = t.localtime()  #调用现在时间，返回一个元组
        ltimestart = list(timestart) #转化为一个时间列表
        self.dictstart = dict(day = ltimestart[7], hour = ltimestart[3], minu = ltimestart[4], seco = ltimestart[5]) #把需要的数据一年的天数，小时，分，秒传入一个字典
        self.secstart = self.dictstart['day'] * 86400 + self.dictstart['hour'] * 3600 + self.dictstart['minu'] * 60 + self.dictstart['seco'] #计算出现在是一年的多少秒
    def stop(self):
        if not self.countstart: #调用停止的条件是，已经调用过开始
            print('Please start the timer first.')
        else:
            print('Timer is stopped')
            timestop = t.localtime() #同理与调用开始一样的数据，计算出停止时是一年的多少秒
            ltimestop = list(timestop)
            self.dictstop = dict(day = ltimestop[7], hour = ltimestop[3], minu = ltimestop[4], seco = ltimestop[5])
            self.secstop = self.dictstop['day'] * 86400 + self.dictstop['hour'] * 3600 + self.dictstop['minu'] * 60 + self.dictstop['seco']
    def __repr__(self): #此方法是能够在系统内部打印出字符串，而且一定要有字符串返回，直接调用对象的时候就会返回相应的字符串
        try: #如果没有计时开始和计时结束，调用这个方法就会报错，所以这里要处理异常
            self.timelast = self.secstop - self.secstart
            return ('The time lasts %d seconds.' % self.timelast)
        except: #如果有异常，就会提示
            return ('Please start/stop the timer.')
        
    def __add__(self, other):#这里实现了实例化对象的相加
        return ('The time lasts %d seconds.' % (self.timelast + other.timelast))






                
