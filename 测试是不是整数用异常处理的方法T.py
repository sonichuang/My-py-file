#从这个程序可以看到，当有异常出现时，直接跳到except,而不会执行有异常语句后面的代码
def int_input():
    while True:
        try:
            m = int(input('Please input a integer:'))#当有异常出现时，直接跳到except.如果没有异常则继续下面的代码。
            break
        except ValueError as reason:
            print('There is problem', reason, 'Input is wrong, input again.')


int_input()
