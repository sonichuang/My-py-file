#我通过os.path.isfile()这个方法找到文件夹，然后通过os.path.getsize()来计算出所有文件的大小
import os
def filesize(path):
    os.chdir(path)
    allfiles = os.listdir()
    for eachfile in allfiles:
        if os.path.isfile(eachfile):
            size = os.path.getsize(eachfile)
            print(' %s ==>> %d.' % (eachfile, size))

path = input('Input the path:')
filesize(path)
        
            



