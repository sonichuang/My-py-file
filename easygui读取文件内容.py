import easygui as g
import os
import sys
path = 'E:\\test'
while 1:
    root = g.fileopenbox('请选择您需要打开的文本文件', default = path)
    if root != None:
        ext = os.path.splitext(root)[1]
        filename = os.path.basename(root)
        if ext != '.txt':
            a = g.ccbox('【%s】不是文本文件，请点【重新选择】, 或者点击【退出】或关闭窗口退出程序。'% filename, '出错了！', ('【重新选择】', '【退出】'))
            if a == True:
                path = os.path.dirname(root)
                continue
            else:
                sys.exit() 
        else:
            f = open(root, 'r')
            content = f.read()
            f.close()
            b = g.ccbox('是否要读取【%s】' % filename, choices = ('【读取】', '【重新选择】'))
            if b == True:
                g.textbox('文件【%s】的内容如下：' % filename, '显示文件内容', content)
                sys.exit()
            elif b == False:
                path = os.path.dirname(root)
                continue
            else:
                sys.exit()
    else:
        sys.exit()
