import random as r

legal_x = [0, 10]#范围的最大值和最小值
legal_y = [0, 10]

class Turtle:#定义乌龟的类
    def __init__(self):#初始化属性
        # 初始体力
        self.power = 100 #初始化体力为100
        # 初始位置随机。x轴在0到10，y轴从0到10
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self): #定义移动的方法
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
            #如果小于0, 则相反方向移动到同样距离零点的距离
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
            #如果大于10,同理
        else:
            self.x = new_x #如果位置在范围内，则不变
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y        
        # 体力消耗。移动一部消耗1
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)

    def eat(self):#定义吃鱼的方法。吃掉鱼体能增加20。体能最大为100。
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        
    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 返回移动后的新位置
        return (self.x, self.y)

turtle = Turtle() #实例化乌龟
fish = [] #鱼的列表
for i in range(10):
    new_fish = Fish()#实例化10条鱼。
    fish.append(new_fish) #扔进列表里

while True:
    if not len(fish): #如果鱼的列表为空
        print("鱼儿都吃完了，游戏结束！")
        break
    if not turtle.power: #如果乌龟体能为0
        print("乌龟体力耗尽，挂掉了！")
        break

    pos = turtle.move() #乌龟移动方法返回一个坐标
    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    for each_fish in fish[:]: #对列表进行了拷贝
        if each_fish.move() == pos: #每条鱼一个坐标鱼乌龟的坐标进行对比。有一样的及被吃掉。
            # 鱼儿被吃掉了
            turtle.eat() 
            fish.remove(each_fish) #在原列表中删除这条鱼。
            print("有一条鱼儿被吃掉了...")
