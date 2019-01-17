import easygui as g  
import sys #退出系统需要用到
msg = '【*真实姓名】为必填项。\n【*手机号码】为必填项。\n【*E-mail】为必填项。' #这里\n必须要在整个长字符串内
title = '账号中心'
fields = ['*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ', '*E-mail']
impt = ['*用户名', '*真实姓名','*手机号码', '*E-mail'] #为了更方便迭代，另外用必填项目组成一个列表。
caution = '请注意：带*号项目必填,而且不能有空格！\n电话号码必须为数字。\n请点击OK，重新填写。\n点击Cancel,退出账号中心' #这里文字比较多，所以拿到前面来定义了。 
values = [] #为了防止后面zip打包字典的时候，出现变量没有定义的错误，所以赋值一个空的列表。

while 1:
    values = g.multenterbox(msg, title, fields, values) #为了在后面需要重新输入时，不重复输入之前的数据，就把之前的数据赋值到变量中
    if values == None: #如果用户取消输入和点×，就会给values赋值为None，会导致后面打包字典的时候出现错误。所以要排除
        sys.exit()
    else:
        dict1 = dict(zip(fields, values)) #把两个列表打包成字典
        for i in impt: #迭代出必填项目的键。
            check = dict1.get(i)  #用get导出键值。
            if ' ' in check or check == ''or str(dict1['*手机号码']).isdigit() == False: #判断键值是否为空格，无输入，不是数字
                a = g.ccbox(caution , '账号中心',('OK','Cancel') ) #出现警告语，再选择是否要继续输入，或者取消
                if a == True:
                    break #如果继续输入退出循环到主循环重新输入
                else:
                    sys.exit() #否则退出系统
        else:  #我在这个地方用了for...else.....语句，只有for循环里的条件都不成立的时候，也就是都输入正确后才会执行else后面的代码。
            g.msgbox('输入符合要求，谢谢!')
            sys.exit()
            
