#我的思路是，通过walk方法找到文件和他的路径，再判断是不是视频文件，如果是
#就是对应的路径加上文件名写入新的文件
import os

def findvideo(path):
    for root, dirs, files in os.walk(path):
        for eachfile in files:
            extname = os.path.splitext(eachfile)[1]
            if extname in ['.avi', '.mp4', '.rmvb']:
                file = open(path + os.sep + 'file.txt', 'a+')
                file.write(root + os.sep + eachfile + os.linesep)#os.sep指当前系统下的路径分隔符
                #os.linesep指当前系统下的换行符
    file.close()
                
path = input('Input the root you want to start finding:')
findvideo(path)
        
 
