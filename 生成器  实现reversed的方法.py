'''用生成器实现reversed的功能'''
def myrev(string):
    if isinstance(string, str): #判断参数是否为字符串
        i = -1
        while True: 
            strin = string[i] #从最后一个序列号开始
            yield strin
            i -=1
            if i < -len(string): #如果超过了字符串的长度
                break            
    else:
        print('Argument in myrev() isn\'t string')

t = myrev('tomorrow morning')
for x in t:
    print(x, end = '')

