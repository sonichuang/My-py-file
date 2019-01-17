
def file_replace(file_name, rep_word, new_word):
    f_read = open(file_name)#以只读模式打开

    content = [] #定义一个空的列表
    count = 0

    for eachline in f_read:#调出每一行的内容，一个字符串
        if rep_word in eachline:
            count += 1 #如果有这个字符的话，就记一个数
            eachline = eachline.replace(rep_word, new_word)#把这个字符串相关的内容替换掉
        content.append(eachline)    #然后写入空的列表中

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
                   % (file_name, count, rep_word, rep_word, new_word))

    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(file_name, 'w')#再次以写入的方式打开文件
        f_write.writelines(content)#写入列表中的所有字符串
        f_write.close()

    f_read.close()


file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)
