import os
import easygui as g
import time #导入时间模块
import sys
localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) #time.localtime()返回目前是的时间是time.struct_time(tm_year=2018, tm_mon=8, tm_mday=14, tm_hour=23, tm_min=25, tm_sec=22, tm_wday=1, tm_yday=226, tm_isdst=0)
root = g.diropenbox('选择需要统计的文件夹', default = 'E:/python files/IDEL FILES') #用easygui定义要开始查找的目录
countlines = 0 #要叠加所以先赋值为零
countfiles = 0
if root == None:
  sys.exit()
for each in os.walk(root): #用迭代的方法找到每个目录下的路径，目录列表和文件列表组成的元组
  a = each[0] #找到元组的第一个元素，及路径的字符串
  b = each[2] #找到元组的第三个元素，文件名列表
  for i in b: #再迭代出文件名列表中的每个文件名的字符串
    if os.path.splitext(i)[1]=='.py' and 'T' not in i: #要求文件名的扩展名为.py和文件名中没有T
    	print(i) #打印出这些文件名
    	countfiles += 1 #叠加计算出总的文件数
    	eachroot = a + '/' + i #组合成文件的具体地址
    	with open(eachroot, 'r', encoding = 'UTF-8') as f: #打开这个文件
    		list1 = list(f) #用列表的方法导出文件内容
    		list1 = [i for i in list1 if i != '\n'] #用列表解析法删除代码中的空行
    		lines = len(list1) #由于文件内容的列表每一个元素就是文件中的一行代码，所以用len的方法就得出这个文件的代码行数
    	countlines += lines #再叠加得到总的代码量
left = 10**5 - countlines #离一万行的距离就在这里
with open('coding recorde.txt', 'a') as f:
    f.write('到%s为止,共写了【%d】个文件【%d】行代码,离十万行还有【%d】行。\n' % (localtime,countfiles, countlines, left))

print('到%s为止,共写了【%d】个文件【%d】行代码,离十万行还有【%d】行。' % (localtime,countfiles, countlines, left))#输出结果
    		
