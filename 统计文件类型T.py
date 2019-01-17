#老师根据字典的键和值来实现这个程序
import os

all_files = os.listdir(os.curdir) # 使用os.curdir表示当前目录更标准，得到当前目录的所有文件的列表.
type_dict = dict()#定义一个空的字典

for each_file in all_files:#迭代每个文件
    if os.path.isdir(each_file):#如果each_file是directory目录
        type_dict.setdefault('文件夹', 0)#如果字典里面没有文件夹这个键就第一个初值为0，如果有文件夹这个键则返回它的值
        type_dict['文件夹'] += 1#累加1,有多少文件夹它的键的值就为多少
    else: #如果不是文件夹
        ext = os.path.splitext(each_file)[1]#分离出每个文件的扩展名(第一个索引值就是扩展名)
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1 #同上面文件夹的方法，用字典键和值的方法可以首次赋值，又可以在变量ext等于不同的键时储存它的值，也就是当文件扩展名再此出现时，它会自动等于以前所赋的值，再累加1.这个方法很实用。

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))#最后再通过字典的方法得出对应键的值
