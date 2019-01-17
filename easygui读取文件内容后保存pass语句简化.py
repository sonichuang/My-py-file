def askcontinue():
    askcontinue = g.ccbox('是否要继续选择其他文件，或者退出程序?' , choices = ('【继续选择】', '【退出程序】') ) #取消读取后选择是否需要继续选择还是退出程序
    if askcontinue == True:
        path = root #如果继续选择，就把文件的路径赋值给fileopenbox的参数，以打开最近的文件夹
        pass
    else:
        sys.exit() #如果选择退出程序或者取消

def savenewpath():
    dest = g.filesavebox('请在下方输入您想保存的文件名。', '另存为', default = 'E:\\test\\*.txt', filetypes = ['*.txt', '*.pdf', '*.py', '*.doc']) #filesavebox运行时会让用户选择位置并输入文件名，文件名需要输入扩展名，可以预先用通配符如：'*.txt' 定义default参数，点击确定后返回这个文件的地址，filetypes会让用户选择文件类型。
    if dest != None: #如果没有点击取消或者×关闭窗口，返回了地址和文件名
        if '.txt' not in dest: #如果没有txt在返回路径中说明不是保存的文本文件或者没有扩展名
            tuple = os.path.splitext(dest)#splitext返回的是一个含有路径加文件名的字符串和文件扩展名的字符串组成的元组
            ext = tuple[1] #提出扩展名
            extname = ext.replace('.','') #删掉圆点
            if extname == '': #如果没有扩展名
                extname = '空'
            askext = g.ccbox('扩展名为【%s】的文件不是文本文件。\n您是否要继续保存为扩展名为【%s】的文件，还是要保存为文本文件？' % (extname, extname), choices = ('保存为扩展名为【%s】的文件' % extname, '保存为文本文件'))#格式化这里，前面有几个格式化字符，后面就要有多少个变量
            if askext == True: #继续保存为非文本文件
                with open(dest, 'w') as fnw: #在保存地址新建文件并写入对应的内容
                    fnw.write(read)
                    askcontinue()                                
            elif askext == False: #选择要保存为文本文件
                dest = tuple[0] + '.txt' #元组的第一个字符串是路径加文件名，然后后后面的.txt组成新的文件地址
                with open(dest, 'w') as fnw:#在保存地址新建文件并写入对应的内容
                    fnw.write(read)
                    askcontinue()
            else: #被取消或者点击×
                askcontinue()
        else: #如果是文本文件就直接写入文件
            with open(dest, 'w') as fnw:
                fnw.write(read)
                askcontinue()
    else:#如果用户此时取消了操作。
        askcontinue()
    
        
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
        askread = g.ccbox('是否要读取【%s】' % filename, choices = ('【读取】', '【重新选择】')) #确认是否要读取还是重新选择
        if askread == True: #如果是读取
            read = g.textbox('文件【%s】的内容如下：' % filename, '显示文件内容', content) #textbox显示文件的文件内容是可以进行修改的，当点击确定后返回的值是修改后的内容。
            if read == None: #如果用户点取消或者×按钮，就会返回None.
                askcontinue()
            elif read != content: #如果读取后的内容被修改了。
                asksave = g.buttonbox('检测到文件内容发生了改变，请选择以下操作：', '警告', ('覆盖保存', '放弃保存', '另存为')) #buttonbox有三个选项，会返回选项的内容，点击×返回None.
                if asksave == '覆盖保存': #点击了覆盖保存
                    fn = open(root,'w') #以写入的方式打开原文件
                    fn.write(read) #在原文件中写入修改后内容
                    fn.close() #关闭文件
                    askcontinue()
                elif asksave == '另存为': #点击另存为
                    savenewpath()
                else:#点击取消保存或者×关闭窗口
                    askcontinue()
            else:#如果没有对文件内容做任何修改。
                asksave = g.buttonbox('请选择以下操作：', choices = ('放弃保存', '另存为')) #buttonbox有两个选项，会返回选项的内容，点击×返回None.
                if asksave == '另存为':
                    savenewpath()
                else: #如果点击放弃保存
                    askcontinue()
        elif askread == False: # 如果选择不读取文件而是重新选择
            path = root #赋值给fileopenbox的参数以重新打开最近的文件夹
            continue
        else:
            sys.exit() #如果不读取又被关闭窗口
    else: #如果一开始就选择了退出
        sys.exit() 

