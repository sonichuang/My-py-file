#老师还是通过字典映射的方法，键为文件，值为文件的大小。
import os

all_files = os.listdir(os.curdir) # 使用os.curdir表示当前目录更标准
file_dict = dict()

for each_file in all_files:
    if os.path.isfile(each_file):#定义所有文件，而不是文件夹
        file_size = os.path.getsize(each_file)#所有文件的大小
        file_dict[each_file] = file_size#添加含有文件名和文件大小的items

for each in file_dict.items():
    print('%s【%dBytes】' % (each[0], each[1]))
