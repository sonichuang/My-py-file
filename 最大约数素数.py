def max(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('%d 的最大约数是 %d。' % (num, count))
            break
        count -= 1
    else:
        print('%d 是素数。' % num)

max(int(input('输入一个数：')))
    
