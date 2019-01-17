import math

def is_prime(number):#判断一个数是否是素数
    if number > 1:
        if number == 2:#如果等于2是素数
            return True
        if number % 2 == 0:#number如果是偶数排除
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):#number如果是奇数，而奇数的因数永远不是偶数，所以步数为2，被除数也是奇数
            if number % current == 0:#所以这些奇数中有number的因数就排除
                return False 
        return True 剩余的奇数是素数
    return False 剩余1不是素数

def get_primes(number):#生成素数的机器叫素数生成器
    while True:
        if is_prime(number):#如果是素数，就返回值
            yield number
        number += 1 #再叠加1

def solve(): #把素数叠加
    total = 2#第一个数是2
    for next_prime in get_primes(3):#从3开始的素数中
        if next_prime < 100: #范围小于100
            total += next_prime
        else: #完事后
            print(total)
            return#结束

if __name__ == '__main__':
    solve()
