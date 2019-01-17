import os
#第三个被调用的函数
def print_pos(key_dict):#包含主函数的变量：包含
    keys = key_dict.keys() #调出该路径下文件包含有关键字的行数
    keys = sorted(keys) # 由于字典是无序的，我们这里对行数进行排序
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key])))#从字典中调出对应行数的值：位置列表

#第二个被调用的函数
def pos_in_line(line, key):#定义函数 每一行内容的字符串 和 关键字
    pos = []
    begin = line.find(key)#找到第一个关键字的位置，如果没有找到就返回-1
    while begin != -1: #如果有找到第一个就继续找
        pos.append(begin + 1) # 用户的角度是从1开始数。如果有找到就在空的列表里写入关键字的位置
        begin = line.find(key, begin+1) # 从下一个位置继续查找

    return pos 返回每一行字符串中关键的位置列表

#第一个需要调用的函数
def search_in_file(file_name, key): #变量包含一个路径，和关键字
    f = open(file_name) #以只读模式打开文件
    count = 0 # 记录行数
    key_dict = dict() # 字典，用户存放key所在具体行数对应具体位置
    
    for each_line in f:#遍历文件每一行
        count += 1 #开始数有多少行
        if key in each_line: #如果关键字在这行
            pos = pos_in_line(each_line, key) #调用函数 返回每一行字符串中关键的位置列表并赋值给一个变量
            key_dict[count] = pos #在空的字典中写入含有关键字的行数键值和对应的值：位置列表
    
    f.close()#关闭文件
    return key_dict #返回该路径下文件中含有关键字的行数和对应位置列表的字典

#主函数
def search_files(key, detail): #定义两个变量关键字和是否搜索
    all_files = os.walk(os.getcwd()) #用walk方法列出每个目录下的路径，所有文件夹列表，所有文件列表的三元组
    txt_files = []

    for i in all_files:# 遍历出每个三元组
        for each_file in i[2]:#each_file从每个三元组的第三部分：所有文件列表中遍历出每个文件名，each_file及为每个文件名
            if os.path.splitext(each_file)[1] == '.txt': # 根据后缀判断是否文本文件 分割出第二部分为文件的扩展名
                each_file = os.path.join(i[0], each_file) #给each_file重新赋值为三元组的第一部分：路径， 再加上文本文件名
                txt_files.append(each_file) #在空的列表中写入每个文本文件的路径

    for each_txt_file in txt_files: #遍历出每个文本文件的路径
        key_dict = search_in_file(each_txt_file, key)#调用第一个函数，返回该路径下文件中含有关键字的行数和对应位置列表的字典，并赋值给一个变量
        if key_dict:#如果字典不为空
            print('================================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
            if detail in ['YES', 'Yes', 'yes']:
                print_pos(key_dict) #调用第三个函数 打印出该路径下文件包含关键字的行数和对应的位置列表


key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
search_files(key, detail)
