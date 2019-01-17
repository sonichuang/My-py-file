import easygui as g
import os

def show_result(start_dir):
    lines = 0 #是个局部变量，其实这里赋值为零，并没有在计算中起到作用，这里更多的是一个声明的作用，表示这里有一个变量，初始化一下。
    total = 0
    text = ""

    for i in source_list: #直接迭代出字典的键
        lines = source_list[i] #对应的映射键值，即对应文件类型的代码行数.
        total += lines #总行数
        text += "【%s】源文件 %d 个，源代码 %d 行\n" % (i, file_list[i], lines) #file_list的键也是i, 对应键值是文件个数。
    title = '统计结果'
    msg = '您目前共累积编写了 %d 行代码，完成进度：%.2f %%\n离 10 万行代码还差 %d 行，请继续努力！' % (total, total/1000, 100000-total) #%.2f %%第一个百分号和 .2f 相连，表示浮点数类型保留小数点后两位格式化输出；然后的两个连续的%%，则最终会输出一个%号出来，有对%进行转义的含义；
    g.textbox(msg, title, text)

def calc_code(file_name):#用局部变量做参数
    lines = 0
    with open(file_name) as f: #老师这里没有定义解码方式所以导致用Idle直接写的代码无法读取，所有会不准确。只能读取全英文的代码.
        print('正在分析文件：%s ...' % file_name)
        try:
            for each_line in f:
                print(each_line)
                lines += 1 #迭代出每一行，再叠加计算出总的行数
        except UnicodeDecodeError:
            pass # 不可避免会遇到格式不兼容的文件，这里忽略掉......老师这里避免报错
    return lines #返回总行数

def search_file(start_dir) : #定义函数的时候用变量名start_dir,但是在主代码里用主代码的变量名path
    os.chdir(start_dir) #定义工作目录
    
    for each_file in os.listdir(os.curdir) : #迭代出工作目录的所有文件名
        ext = os.path.splitext(each_file)[1] #再迭代出文件名的扩展名。
        if ext in target : #如果扩展名是我们需要统计的文件类型
            lines = calc_code(each_file) # 统计行数
            # 还记得异常的用法吗？如果字典中不存，抛出 KeyError，则添加字典键
            # 统计文件数
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
            # 统计源代码行数.第一次统计的时候，键不存在抛出异常，在except处开始给键赋值
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines
            #用这种方法可以多任务同时统计上面source_list, file_list都是全局变量，但是是可变对象，在函数中可以对他们直接进行修改，而不必用global进行声明。
        if os.path.isdir(each_file) :#如果是文件夹，则进入文件夹
            search_file(each_file) # 递归调用
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录
            
target = ['.c', '.cpp', '.py', '.cc', '.java', '.pas', '.asm']
file_list = {}
source_list = {}

g.msgbox("请打开您存放所有代码的文件夹......", "统计代码量")
path = g.diropenbox("请选择您的代码库：")

search_file(path)
show_result(path)
