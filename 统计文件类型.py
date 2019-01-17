#我的思路是：先分离出所有文件的扩展名，然后把所有扩展名加入进一个空集合自动形成一个不重复的集合，
#再把所有文件扩展名组成一个列表，然后再从集合里面分别迭代出一个元素，再到列表里面去数，看有多少个
#元素，从而得出有多少个这种扩展名的文件

def count(path):
    os.chdir(path) #修改工作目录到指定目录
    allext = set([]) #新建一个空集合，利用它的不重复的特征
    allhave = [] #新建一个空的列表

    for eachfile in os.listdir(): #列出指定目录下的文件名和文件名
        (name, ext) = os.path.splitext(eachfile) #分离出文件的扩展名
        allext.add(ext) #把所有扩展名加入空的集合，并会删掉重复
        allhave.append(ext) #把所有的扩展名写入空的列表
    for eachext in allext: #迭代出集合里的扩展名
        n = allhave.count(eachext)#输出某一个扩展名有多少个
        if eachext == '': #如果是文件夹，扩展名为空
            eachext = 'folders' #指明是文件夹
        print('There have %d \'%s\'.' % (n, eachext))#再把打印出来
     
import os
while True:
    path = input('Input the path:')
    if os.path.exists(path) == True: #判断指定路径是否存在
        count(path)
    elif path in 'Exitexit':#如果输入exit退出系统
        break
    else:
        print('Path is wrong, input the correct path.')
    
    
