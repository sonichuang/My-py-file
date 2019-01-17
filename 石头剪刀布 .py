import easygui as g
import sys
import random as r 
time = 10
win = 0
def judge(a, b): #对对决的结果进行判断
    if a == '剪刀' and b == '布':
        return '你输了！'
    if a == '剪刀' and b == '石头':
        return '你赢了！'
    if a == '石头' and b == '布':
        return '你赢了！'
    if a == '石头' and b == '剪刀':
        return '你输了！'
    if a == '布' and b == '石头':
        return '你输了！'
    if a == '布' and b == '剪刀':
        return '你赢了！'
    if a == b:
        return '平手！'
    
def final(t, w): #对结局进行判断
    if w == 6:#如果先赢了6次，就算赢
        askplay = g.ccbox('现在的比分为 %d : %d，\n这一局，你赢了！' % (10-t-w, w), '石头-剪刀-布1.0版', ('再来一局', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\youwin.png')
        if askplay == True: #如果选择再来一次
            return 'continue' #这里只是一个信号，返回一个字符串，当主程序收到这个字符串是会对t,w变量初始化，由于是局部变量不能在函数里面进行初始化，所以要移到主程序。
        else: #如果选择退出
            sys.exit()
    if t == 0 and w == 5:#如果10次，最后只赢了5次，平局
        askplay = g.ccbox('现在的比分为 %d : %d，\n这一局，我们是平局！' % (10-t-w, w), '石头-剪刀-布1.0版',('再来一局', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\tie.png')
        if askplay == True:
            return 'continue'
        else:
            sys.exit()
    if (10-t-w) == 6:#如果先输了6次，就输
        askplay = g.ccbox('现在的比分为 %d : %d，\n这一局，你输了！' % (10-t-w, w), '石头-剪刀-布1.0版', ('再来一局', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\final lose.png')
        if askplay == True:
            return 'continue' 
        else:
            sys.exit()

askplay = g.ccbox('我们来一个石头，剪刀，布的游戏吧！', '石头-剪刀-布1.0版', ('开始游戏', '不想玩儿了'), image = 'E:\\python files\\IDEL FILES\\picture\\game.png')
if askplay == True:#如果选择开始游戏
    askplay = g.ccbox('游戏规则：\n10次有效出牌,先胜6次即为胜出本局，\n如果双方出一样的牌即为无效出牌,\n注意：点击图片会退出游戏', '石头-剪刀-布1.0版', ('开始游戏', '不想玩'), image = 'E:\\python files\\IDEL FILES\\picture\\rules.png')
    if askplay == True:
        while time:#循环
            syschoice = r.choice(['剪刀', '布', '石头'])#random.choice(sequence)可以随机选择一个元素，sequence序列可以是字符串，列表，元组
            mychoice = g.buttonbox('请出牌', '石头-剪刀-布1.0版', ('剪刀', '布', '石头'), image = 'E:\\python files\\IDEL FILES\\picture\\game.png')
            result = judge(syschoice, mychoice)#判断出盘结果
            if result == '你赢了！':
                time -= 1 #次数少一
                win += 1 #赢一次
                if final(time, win) == 'continue': #对是否一局结束局进行判断，并得出结果，如果有收到指令'continue'
                    time = 10 #初始化
                    win = 0
                    continue #结束当前循环，开始下轮循环，并对条件进行判断
                askplay = g.ccbox('我出的『%s』，你出的『%s』\n有你的，你赢了！\n现在的比分为 %d : %d，还可以出牌 %d 次。' % (syschoice, mychoice,10-time-win, win, time), '石头-剪刀-布1.0版', ('再出牌', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\you win.png')#如果出牌赢了
                if askplay == True: #继续出牌
                    continue
                else:
                    sys.exit()
            if result == '你输了！':#如果出牌输了
                time -= 1
                if final(time, win) == 'continue':#同样判断是否一局结束，并得出结果，收到指令后初始化
                    time = 10
                    win = 0
                    continue
                askplay = g.ccbox('我出的『%s』，你出的『%s』\n呵呵，你输了！\n现在的比分为 %d : %d，还可以出牌 %d 次。' % (syschoice, mychoice,10-time-win, win, time), '石头-剪刀-布1.0版', ('再出牌', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\you lose.png')#出牌输了
                if askplay == True:#如果要继续出牌
                    continue
                else:
                    sys.exit()
            if result == '平手！': #单次出牌打成平手
                askplay = g.ccbox('我出的『%s』，你出的『%s』\n不错哦，跟我打成平手！\n现在的比分为 %d : %d，还可以出牌 %d 次。' % (syschoice, mychoice,10-time-win, win, time), '石头-剪刀-布1.0版', ('再出牌', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\tied.png')
                if askplay == True:
                    continue
                else:
                    sys.exit()
            if result == None:#如果选择退出游戏
                sys.exit()
    else:
        sys.exit()
else:
    sys.exit()

