import os

#主函数
def searchcontent(path, substr): #主函数包含两个变量，开始路径和关键字
    for root, dirs, files in os.walk(path): #找到所有的路径和文件名列表
        for eachfile in files:#找出每个文件名
            extname = os.path.splitext(eachfile)[1]#分割文件名的扩展名
            if extname == '.txt':#看是否是文本文件，如果是文本文件
                file = open(path + os.sep + 'file.txt', 'a+')#创建一个开始路径下的file文件
                file.write(root + os.sep + eachfile + os.linesep)#写入该路径下的文件全路径并换行
    file.seek(0, 0) #在a+模式写入的文件，指针总是处在文件末尾，所有需要把指针调到文件开头
    for filepath in file:#遍历每一行的文件路径
        (realpath, n) = filepath.split('\n')#把换行符分割出来，因为换行符总是在末尾会分割成一个路径字符串和一个空的字符串，而且每行之间还有一个换行符，这一行会分割成两个空字符串，所以要排除这一行
        if realpath != '':#不为空字符串
            eachfile = open(realpath, 'r+')#把这个文本文件打开
            if substr in eachfile.read():#如果里面含有关键字，才继续下面的工作，这样节约资源
                eachfile.seek(0, 0)#指针定位到文件开始位置
                print('In path \'%s\', \'%s\' is in' % (realpath, substr))
                countline = 0 #开始数行数
                for eachline in eachfile:#文件的每一行
                    countline += 1
                    if substr in eachline:#如果这一行含有关键字
                        print('%d line NO %s' % (countline, findeachlineindex(eachline, substr)))#调用函数返回这一行关键字位置的列表
                    
                    
def findeachlineindex(eachline, substr):# 被调用函数，包含有两个变量一个是主函数的变量：一行的内容字符串，一个是关键字
    count = 1
    indexlist = []
    while count:
        if count == 1:
            index = eachline.find(substr)#先找到这一行第一个关键字的位置
            count += 1
        else:
            index = eachline.find(substr, index+1)#从下一个位置开始找，直到找完为止，返回值-1结束循环
            if index == -1:
                break
        indexlist.append(index) #把这一行关键字的位置写入空的列表
    return indexlist #函数返回这一行关键字位置的列表

path = input('Input the root you want to start finding:')
substr = input('Input the substring you want to find:')
searchcontent(path, substr)
        
 
