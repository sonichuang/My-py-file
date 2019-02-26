'''本脚本是利用easygui提供的交互程序在placekitten.com下载喵星人图片'''
import urllib.request as ur
import easygui as eg
import os
#基础信息，默认尺寸
msg = '输入图片尺寸'
title = '喵星人图片下载 v1.0  Developer:SonicHuang'
length = '400'
width = '600'

while True:
    size = eg.multenterbox(msg, title, ['长', '宽'], [length, width])
    if size != None and size[0] != '' and size[1] != '':
        length = size[0]
        width = size[1]
        url = ''.join(['http://placekitten.com/g/', length, '/', width])
        #处理网络异常和输入错误
        try: #int()的参数必须为整数
            int(length)
            int(width)
            response = ur.urlopen(url)
        except: #提示异常信息并返回主循环重新输入
            eg.msgbox( '出错了！请检查输入的数据(必须为整数)和检查网络是否连接.', title, 'OK')
            continue
        else:
            #直接读取图片，并保存为一个临时图片
            catimage = response.read()
            with open('temp.jpg', 'wb') as f1:
                f1.write(catimage)
            #预览临时图片
            asksave = eg.buttonbox('预览\n需要保存请点击图片', title, ('保存图片', '重新输入尺寸', '退出'), 'temp.jpg')
            #删除临时文件再保存图片，如果点击了图片会返回图片名
            if asksave == '保存图片' or asksave == 'temp.jpg':
                os.remove('temp.jpg')
                savepath = eg.filesavebox('选择需要保存的位置', title = title, default = 'newimage.jpg', filetypes = ['*.jpg'])
                if savepath == None:#点击取消或者X返回None
                    ask = eg.buttonbox('要继续下载吗?', title, ('继续', '退出'))
                    if ask == '继续':
                        continue
                    else:
                        break
                else:
                    with open(savepath, 'wb') as f:
                        f.write(catimage)
                    ask = eg.buttonbox('要继续下载吗?', title, ('继续', '退出'))
                    if ask == '继续':
                        continue
                    else:
                        break
            #如果不喜欢这个图片或者尺寸，删除之前的临时图片，再重新输入尺寸
            elif asksave == '重新输入尺寸':
                os.remove('temp.jpg')
                continue
            #退出时也要删除临时文件
            else:
                os.remove('temp.jpg')
                break
    elif size == None:#退出
        break
    else:#输入错误时
        feedback = eg.buttonbox('输入错误，请重新输入?', title, ('重新输入', '退出'))
        if feedback == '重新输入':
            continue
        else:
            break


