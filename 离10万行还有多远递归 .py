def findpy(root): #定义函数
    global countlines #定义全局变量。函数可以访问全局变量，但是不能修改全局变量，如果要修改就得把局部变量定义为全局变量。
    global countfiles #定义全局变量。
    filelist = os.listdir(root) #列出工作目录下文件夹下的文件和文件夹。但是再进入文件夹，就只能列出文件夹下的文件名，而不能进行判断。
    os.chdir(root) #改变工作目录，注意如果这里不定义工作目录，系统只能判断工作目录下的文件和文件夹，再进入文件夹就不能判断了，除非用该文件夹的详细地址。
    for each in filelist: #迭代出所有的文件和文件夹进行判断
        if '.py' in each and 'T' not in each: #只要是我写的代码文件。
            print(each)
            countfiles += 1 #叠加计算出文件个数
            with open(each, 'r', encoding = 'UTF-8') as f: #打开这个文件
                    list1 = list(f) #用列表的方法导出文件内容
                    list1 = [i for i in list1 if i != '\n'] #用列表解析法删除代码行的空行
                    lines = len(list1) #由于文件内容的列表每一个元素就是文件中的一行代码，所以用len的方法就得出这个文件的代码行数
            countlines += lines #再叠加得到总的代码量
        if os.path.isdir(each): #判断如果是文件夹
            findpy(each)#进入工作目录里的文件夹进行递归算法
            os.chdir(os.pardir)#进入工作目录下的文件夹后要退到原工作目录里才能形成完整的递归
            
countlines = 0 #全局变量
countfiles = 0
import os
import easygui as g
import time #导入时间模块
import sys
localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) #time.localtime()返回目前是的时间是time.struct_time(tm_year=2018, tm_mon=8, tm_mday=14, tm_hour=23, tm_min=25, tm_sec=22, tm_wday=1, tm_yday=226, tm_isdst=0)
root = g.diropenbox('选择需要统计的文件夹', default = 'E:/python files/IDEL FILES') #用easygui定义要开始查找的目录
if root == None:
  sys.exit()
findpy(root)
left = 10**5 - countlines #离一万行的距离就在这里
with open('coding recorde.txt', 'a') as f:
    f.write('到%s为止,共写了【%d】个文件【%d】行代码,离十万行还有【%d】行。\n' % (localtime,countfiles, countlines, left))
print('到%s为止,共写了【%d】个文件【%d】行代码,离十万行还有【%d】行。' % (localtime,countfiles, countlines, left))#输出结果
