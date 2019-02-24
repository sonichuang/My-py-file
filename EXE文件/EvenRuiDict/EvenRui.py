'''本脚本是利用easygui的交互界面和youdao.py模块实现简单的词典功能。基于有道在线词典'''
import easygui as eg
import youdao as yd

#定义相关参数，初始的输入框值为空白
msg = '请输入你想查询的单词或句子\n支持英语，中文等'
title = 'EvenRui小词典 v1.0   开发者:SonicHuang'
words = ''
meaning = ''
while True:
    m = eg.multenterbox(msg, title,['请输入：', '意思是：'],[words, meaning])
    if m != None and m[0] != '' and m[1] == '': #输入正确的状态是首先m的值不为None,在输入框有值，在'意思是'这一栏是空白.
        words = m[0]#再赋值给multenterbox的两个参数，使其同时显示单词和他的翻译结果。
        meaning = yd.translate(words)
        m = eg.multenterbox(msg, title,['请输入：', '意思是：'],[words, meaning])
        if m == None: #再点击cancel或者X者退出程序
            break
        else: #点击ok 继续查询，参数为空白回到原始状态
            words = ''
            meaning = ''
            continue
    else: #输入错误时，错误提示
        ask1 = eg.buttonbox('输入错误，请在正确的位置重新输入。', title, ('重新查词', '退出词典'))
        if ask1 == '重新查词':
            words = ''
            meaning = ''
            continue
        else:
            break
        
        
        
