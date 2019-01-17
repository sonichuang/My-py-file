class Sonic:
    mood = '高兴'
    time = '现在'
    plan = '学习编程'
    weather = '天晴'
    def goal(self):
        print('学习Python，立足未来。')
    def setplan(self):
        self.time = input('时间：')
        self.weather = input('天气：')
        self.mood = input('心情：')
        self.plan = input('计划：')
    def myplan(self):
        print('%s的天气%s,心情%s,打算%s。' % (self.time, self.weather, self.mood, self.plan))

    
me = Sonic()
me.setplan()
