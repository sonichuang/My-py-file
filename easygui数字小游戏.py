def compare(guess, secret): #定义一个比较猜的数和答案之间大小的函数
    if guess > secret:
        return  '大'
    if guess < secret:
        return '小'

import easygui as g
import random
i = 1 #定义为1是为了能够是while循环运行
count = 3 #定义了猜的次数
secret = random.randint(1, 9)
guess = g.integerbox('不妨猜一下我现在心里想的是那个数字(1 - 9)，机会只有3次', '数字小游戏', image = 'E:\\python files\\IDEL FILES\\picture\\guess.png', lowerbound=1, upperbound=9) #虽然图片是gif格式但是只能显示第一帧。
while i and guess != None: #当没有被取消，i为True
        count -= 1 #次数叠减
        if guess != secret and count > 0: #如果猜错了，但是还有次数的情况下
            result = compare(guess, secret) #比较这两个数
            
            guess = g.integerbox('你猜的数字%s了,请重新猜,还有%d次机会。' % (result, count), '数字小游戏',image = 'E:\\python files\\IDEL FILES\\picture\\try again.gif', lowerbound=1, upperbound=10) #猜错了，重新猜
        elif count == 0 and guess != secret: #注意这里，当最后一次机会用完后，前面count叠减后为零，但是还在循环体以内，循环还是在继续，现在就要在这种情况下，程序该如何走。还是没有猜对要怎么样？
            i = 0 #这里马上把i赋值为零跳出循环。注意在这里不能用break,因为在这里使用了while..else..语句，如果使用break语句也就是while循环没有完成就直接中断，那么就不会执行后面的else语句，但是在这里给i赋值为0，执行完while所有语句后间接的中断了循环体，而继续执行后面的else语句。
        else: #猜对了
            g.msgbox('恭喜您，答对了！答案是：%d' % secret, '数字小游戏',image = 'E:\\python files\\IDEL FILES\\picture\\congratulation.gif' )
            break #当猜对了的情况下直接中断循环，结束程序。
            

else: #当取消了猜测和机会用完了而没有猜对才会执行到这里来
    if guess == None: 
        g.msgbox('您放弃了？下次再来吧！答案是：%d' % secret, '数字小游戏', image = 'E:\\python files\\IDEL FILES\\picture\\i quit.gif')
        
    else:
        g.msgbox('机会已经用完，下次再来吧！答案是：%d' % secret, '数字小游戏',image = 'E:\\python files\\IDEL FILES\\picture\\game over.gif')


