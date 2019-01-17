def position(pace = 2): #给一个默认参数，但可以随时修改。
    import random as r #调出random模块
    a = r.randint(0, 10) #起始位置横轴0 - 10的范围
    b = r.randint(0, 10) #起始位置纵轴0 - 10的范围
    m = r.randint(-pace, pace) #每次移动的范围向前和向后分别用+ - 来确定
    n = r.randint(-pace, pace)
    a += m #移动一次就叠加一次，但是m和n有正负，及前后
    b += n
    if a <= 0: #当刚好横轴向左移动到边界，或者要超过边界时，就向正的方向移动相同的步数，及被弹回。向正的方向及m的绝对值
        a += abs(m)
    if a >= 10: #同理到边界弹回，到达或者超出最右边边界时，及被弹回反方向同样的步数。
        a -= abs(m)
    if b <= 0: #同理到纵轴下边界弹回
        b += abs(n)
    if b >= 10: #同理到纵轴上边界弹回
        b -= abs(n)
    return (a, b) #返回一个坐标
        
class Role: #定义一个类
    def move(self, step): #类的方法，一个步数参数
        (self.x, self.y) = position(step) #调用函数得到对象的坐标,调用一次就会有新的坐标。
        return (self.x, self.y) # 返回对象的坐标
    
import sys #调用系统模块
t = Role() #实例化对象，生成一个乌龟的对象
f1 = Role() #生成10条鱼的对象
f2 = Role()
f3 = Role()
f4 = Role()
f5 = Role()
f6 = Role()
f7 = Role()
f8 = Role()
f9 = Role()
f10 = Role()
tpower = 100 #默认乌龟的体能为100
F = {f1:f1.move(1), f2:f2.move(1), f3:f3.move(1), f4:f4.move(1), f5:f5.move(1), f6:f6.move(1), f7:f7.move(1), f8:f8.move(1), f9:f9.move(1), f10:f10.move(1)}
#用每条鱼和他的坐标组成一个元素，再生成一个字典
fdead = [] #因为要统计存活的鱼，所以先定义一个被吃掉的鱼空的列表
fm = list(F.values()) #所有鱼的坐标的集合
allfish = list(F.keys()) #所有鱼的集合
while F: #如果字典不为空，及鱼还没有被吃完。
    tm = t.move(2) #乌龟的坐标
    tpower -= 1 #乌龟每走一步消耗一个能量
    if tpower == 0: #如果乌龟能量耗尽。
        fleft = len(list(F.keys())) #看一个还剩多少条鱼。
        print('乌龟体力已经耗尽！') #打印多少条鱼还活着。
        print('还有剩下%d条鱼。' % fleft )
        sys.exit()
    if tpower >= 100:
        tpower = 100
    fm = list(F.values()) #所有鱼的坐标列表
    if tm in fm: #如果乌龟和某条鱼的坐标一样
        fi = [a for a, b in F.items() if b == tm].pop()#用列表解析式找出那条坐标跟乌龟一样的鱼，及被吃掉。
        num = allfish.index(fi) #并找到是最初定义的鱼的索引值
        print('\'%d\'号鱼被乌龟吃了！' % (num + 1)) #打印是第几条鱼被吃掉了。
        tpower += 20 #吃掉鱼后乌龟的能量加20
        fdead += [fi] #被吃掉的鱼扔进列表里。
        F = {k:v for k, v in {f1:f1.move(1), f2:f2.move(1), f3:f3.move(1), f4:f4.move(1), f5:f5.move(1), f6:f6.move(1), f7:f7.move(1), f8:f8.move(1), f9:f9.move(1), f10:f10.move(1)}.items() if k not in fdead}
        #还是用解析式的方法找到剩下的鱼和他们的下一个坐标
else:
    print('鱼被吃光了！') #如果鱼被吃光了




       





    



    
    

        
        
    

                    
            
