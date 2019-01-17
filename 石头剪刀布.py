import easygui as g
import sys
import random as r
time = 10
win = 0
def judge(a, b):
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
    
askplay = g.ccbox('我们来一个石头，剪刀，布的游戏吧！', '石头-剪刀-布1.0版', ('开始游戏', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\game.png')

if askplay == True:
    askplay = g.ccbox('游戏规则：\n10次有效出牌,先胜6次即为胜出本局，\n如果双方出一样的牌即为无效出牌\n', '石头-剪刀-布1.0版', ('开始游戏', '不想玩'), image = 'E:\\python files\\IDEL FILES\\picture\\game.png')
    if askplay == True:
        while time:
            syschoice = r.choice(['剪刀', '布', '石头'])
            mychoice = g.buttonbox('请出牌', '石头-剪刀-布1.0版', ('剪刀', '布', '石头'), image = 'E:\\python files\\IDEL FILES\\picture\\game.png')
            result = judge(syschoice, mychoice)
            if result == '你赢了！':
                time -= 1
                win += 1
                   
                if win == 6:
                    askplay = g.ccbox('现在的比分为 %d : %d，\n这一局，你赢了！' % (10-time-win, win), '石头-剪刀-布1.0版', ('再来一局', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\youwin.png')
                    if askplay == True:
                        time = 10
                        win = 0
                        continue
                    else:
                        sys.exit()
                if time == 0 and win == 5:
                    askplay = g.ccbox('现在的比分为 %d : %d，\n这一局，我们是平局！' % (10-time-win, win), '石头-剪刀-布1.0版',('再来一局', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\tie.png')
                    if askplay == True:
                        time = 10
                        win = 0
                        continue
                    else:
                        sys.exit()

                    
                askplay = g.ccbox('我出的『%s』，你出的『%s』\n有你的，你赢了！\n现在的比分为 %d : %d，还可以出牌 %d 次。' % (syschoice, mychoice,10-time-win, win, time), '石头-剪刀-布1.0版', ('再出牌', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\you win.png')
                if askplay == True:
                    continue
                else:
                    sys.exit()
            elif result == '你输了！':
                time -= 1
                
                if time == 0 and win == 5:
                    askplay = g.ccbox('现在的比分为 %d : %d，\n这一局，我们是平局！' % (10-time-win, win), '石头-剪刀-布1.0版',('再来一局', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\tie.png')
                    if askplay == True:
                        time = 10
                        win = 0
                        continue
                    else:
                        sys.exit()
                if time == 0 and win <= 5 or (10-time-win) == 6:
                    askplay = g.ccbox('现在的比分为 %d : %d，\n这一局，你输了！' % (10-time-win, win), '石头-剪刀-布1.0版', ('再来一局', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\final lose.png')
                    if askplay == True:
                        time = 10
                        win = 0
                        continue
                    else:
                        sys.exit()

                askplay = g.ccbox('我出的『%s』，你出的『%s』\n呵呵，你输了！\n现在的比分为 %d : %d，还可以出牌 %d 次。' % (syschoice, mychoice,10-time-win, win, time), '石头-剪刀-布1.0版', ('再出牌', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\you lose.png')
                if askplay == True:
                    continue
                else:
                    sys.exit()
            else:
                askplay = g.ccbox('我出的『%s』，你出的『%s』\n不错哦，跟我打成平手！\n现在的比分为 %d : %d，还可以出牌 %d 次。' % (syschoice, mychoice,10-time-win, win, time), '石头-剪刀-布1.0版', ('再出牌', '不想玩了'), image = 'E:\\python files\\IDEL FILES\\picture\\tied.png')
                if askplay == True:
                    continue
                else:
                    sys.exit()
                    

                
            
    else:
        sys.exit()
else:
    sys.exit()

