def change():
    name = input('Input the file name:')
    oldword = input('Input the oldword:')
    newword = input('Input the newword:')
    file = open(name, 'r+') #以可读写的方式打开，然后后面才能被写入。
    line = file.read()#读取出来形成一个长的字符串
    n = line.find(oldword)#直接查找有多少个旧的字符
    answer = input('Have %d \'%s\', do you want change all to \'%s\'? (yes/no)' % (n, oldword, newword))
    if answer =='yes':
        line = line.replace(oldword, newword)#直接在长的字符串中直接替换
        file.seek(0, 0)#注意指针位置需要还原到文件头，这样用truncate才能覆盖掉所有的内容。
        file.truncate(0)#此方法的妙处在于不用再次用open打开文件
        file.write(line)#写入替换后的长的字符串
        file.close()
    else:
        file.close()

change()
