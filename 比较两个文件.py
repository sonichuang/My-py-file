#我的做法是分别计算第几行，共有多少行不一样，然后把要打印的内容写入一个文件，最后再读出文件。

def compare(file1name, file2name):

    file1 = open(file1name, 'r')
    file2 = open(file2name, 'r')
    file3 = open('record.txt', 'a') 
    countnumber = 0
    countline = 0
    while 1：
        eachline1 = file1.readline()
        countline += 1
        eachline2 = file2.readline()
        if eachline1 != eachline2:
            file3.write('the NO.%d line is different.\n' % countline)
            countnumber += 1
        if eachline1 == '' or eachline2 == '':
            break
    print('Have %d lines are different.' % countnumber)
    file3 = open('record.txt', 'r')
    print(file3.read())
    file1.close()
    file2.close()
    file3.close()

compare('sonic1.txt', 'sonic2.txt')

    

    




