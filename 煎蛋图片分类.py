#对下载的图片进行分类
import matplotlib.pyplot as plt
from PIL import Image
import os
import time
import shutil
import easygui as eg
import pickle


os.chdir(r'D:\download\pic')
ways = os.walk(r'D:\download\pic')

for each in ways:
    list1 = each[2]   
    for picname in list1:
        img = Image.open(picname) #打开图片数据
        print(picname)
        plt.ion()#自动滚动显示图片并执行相关脚本, 需要与pause()一起使用
        plt.imshow(img)#显示图片
        plt.show()
        plt.pause(1)#暂停等候
        #使用easygui来对图片进行判断，并移动图片到对应文件夹
        like = eg.buttonbox('喜欢的点OK', '', ('OK', '不喜欢'))
        if like == 'OK':
            shutil.move(picname, ''.join(['D:/download/like/', picname]))
        elif like == '不喜欢':
            shutil.move(picname, ''.join(['D:/download/unlike/', picname]))
        else:
            break

plt.close()
        
        
        
        
        
        
