'''生成器实现素数相加, 大于1的自然数中，除了1和本身没有其他因数可以整除的数'''
def primesum(number):
    if isinstance(number, int):
        num = 2
        while True:#除了1和num最外最大的因数不会大于num//2 +1
            for x in range(2, num//2 +1):#这里用到for else循环，for中的条件都不成立才会执行else, 
                if num%x == 0: #break只要条件成立就跳出循环执行后面循环以外的代码
                    break #除了1和sum就是range(2, sum)中的数都不整除就满足素数的条件执行else
            else:
                yield num
            num += 1
            if num >number:
                break
    else:
        print('Argument in primesum() isn\'t int')

t = primesum(100)
su = 0
for i in t:
    su += i
print(su)
    
