'''用生成器实现reversed的功能'''
def myrev(string):
    if isinstance(string, str): #判断参数是否为字符串
       for x in range(len(string)-1, -1, -1): #从大到小迭代出字符串的序列号
           yield string[x]
    else:
        print('Argument in myrev() isn\'t string')

t = myrev('tomorrow morning')
for x in t:
    print(x, end = '')

