print ('.......................Sonic Huang............................')
print ('guess between 1 - 10 猜一个1到10的数')
import random
secret = random.randint(1,10)
guess = 0
guesstimes = 3
while guess !=secret and guesstimes > 0:
    number = input ('Guess one number请输入你猜的数:')
    while number.isdigit() == False:
        print ('sorry, the input is\'s allowed, please input int.输入不合法，请输入整数:', end= '')
        number = input ()
    guess = int (number)
    guesstimes -= 1
    if guess == secret:
        print ('bingo,you are genius真聪明')
        print ('no present但是没有奖励。')

    else:
        if guess > secret:
            print ('hey, bro, it\'s bigger嘿，大了!')
        else:
            print ('hey bro, it\'s smaller嘿，小了')
        if guesstimes > 0:
            print ('try that again再试一下')
        else:
            print ('chance is out机会用完了')
print ('答案是：', secret)                                                    
print ('game over游戏结束！')


