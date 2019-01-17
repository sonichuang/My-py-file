name = input('input the file name:')
file = open(name, 'r')
order = input('input the order:')
splitorder = order.split(':', 1) #通过把输入的命令进行分离，来确定需要显示的行数开始和结束行号
(start, end) = splitorder #同时为两个变量赋值

def totalline():
    n = 0
    for eachline in file:
        n += 1
    return n


def output():
    if start == '' and end == '':
        liststart = 0
        listend = totalline() #这里文件被引用一次，指针位置到了最后
    if start == '' and end != '':
        liststart = 0
        listend = int(end)
    if start != '' and end != '':
        liststart = int(start) - 1
        listend = int(end)
    if start != '' and end == '':
        liststart = int(start) - 1
        listend = totalline()
    file.seek(0, 0) #由于上面文件被引用，指针位置在文件末尾，所有这里需要重新定位指针到文件开头
    contentlist = list(file)
    outputlist = contentlist[liststart : listend]#所有文件内容的列表进行切片
    for each in outputlist:
        print(each)
    file.close()


output()      
    
    
    
