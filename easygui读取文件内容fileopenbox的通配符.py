import easygui as g
import os
import sys
path = 'E:\\test\\*.txt'
while 1:
    root = g.fileopenbox('请选择您需要打开的文本文件', default = path) #fileopenbox只能打开default这个参数的上一级目录
    if root != None: #如果没有直接退出或者取消
        filename = os.path.basename(root) #导出文件名，后面的程序需要显示文件名
        f = open(root, 'r') #打开这个文件
        content = f.read() #并读取内容
        f.close() #关闭文件
        b = g.ccbox('是否要读取【%s】' % filename, choices = ('【读取】', '【重新选择】')) #确认是否要读取还是重新选择
        if b == True: #如果是读取
            a = g.ccbox(content, '文件【%s】的内容如下：' % filename, choices = ('【继续选择】', '【退出程序】') ) #读取后选择是否需要继续选择还是退出程序。也是不选用msgbox的原因
            if a == True:
                path = root #如果继续选择，就把文件的路径赋值给fileopenbox的参数，以打开最近的文件夹
                continue #continue的作用是终止这轮循环，并测试循环条件，然后开始下一轮循环
            else:
                sys.exit() #如果选择退出程序或者取消
        elif b == False: # 如果选择不读取文件而是重新选择
            path = root #赋值给fileopenbox的参数以重新打开最近的文件夹
            continue
        else:
            sys.exit() #如果不读取又被关闭窗口
    else: #如果一开始就选择了退出
        sys.exit() 
