name = input('input the file name:')
linenumber = int(input('how many lines do you want to print?:'))
file = open(name, 'r')

def totalline(): #计算出总共有多少行
    n = 0
    for eachline in file:
        n += 1
    
    return n

def compare(): #比较输入的需要打印的行数与实际文件的行数的大小，如果输入的大于实际行数，
    total = totalline()#则返回实际行数，如果小于实际行数，就返回输入行数
    if linenumber >= total:
        return total
    else:
        return linenumber

def output(name, linenumber):
    file = open(name, 'r')
    min = compare()
    while min: # 通过行数叠减来确定打印的行数，而老师是通过循环行数的次数来决定打印的行数
        content = file.readline()
        print(content)
        min -= 1
    
        



output(name, linenumber)







