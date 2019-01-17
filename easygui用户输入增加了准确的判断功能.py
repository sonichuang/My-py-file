import easygui as g  
import sys #退出系统需要用到
msg = '【*用户名】为必填项。\n 【*真实姓名】为必填项。\n【*手机号码】为必填项。\n【*E-mail】为必填项。' #这里\n必须要在整个长字符串内
title = '账号中心'
fields = ['*用户名', '*真实姓名', '固定电话', '*手机号码', 'QQ', '*E-mail']
impt = ['*用户名', '*真实姓名', '*E-mail'] #为了更方便迭代，另外用必填项目组成一个列表。
values = [] 

while 1:
    caution = '' #源代码是放在循环外面。由于需要对每一必填项目进行判断，我们采取了叠加赋值的方法，所以初值赋值为空。为什么要放在循环内呢？因为如果放在循环外，caution的值就会不断赋值，出现重复。把caution赋值给msg后，再给caution赋值为空，不会影响msg的值。
    values = g.multenterbox(msg, title, fields, values) #为了在后面需要重新输入时，不重复输入之前的数据，就把之前的数据赋值到变量中
    if values == None: #如果用户取消输入和点×，就会给values赋值为None，会导致后面打包字典的时候出现错误。所以要排除
        sys.exit()
    else:
        dict1 = dict(zip(fields, values)) #把两个列表打包成字典
        checkno = dict1['*手机号码'].replace(' ','') #这里用replace的方法删掉所有的空格，而strip只能删掉字符串首尾的空格。
        if checkno.isdigit() == False: #判断除去空格后的字符串是否为数字。注意这里如果isdigit后面不加()，代码不会报错返回一个地址，但是代码确是错误的，会运行错误。
            caution += '电话号码为必填项，且必须全为数字。\n' #对原字符串进行叠加
        for i in impt: #迭代出必填项目的键。
            check = dict1.get(i)  #用get导出键值。
            if check.replace(' ', '') == '': #同样删除所有空格。但是并不要求不可以输入空格
                caution +='%s为必填项。\n' % i
        msg = caution #把所有的报错信息都赋值给multienterbox的参数，这样就会显示在原输入框中。
        if msg == '': #如果没有报错
            g.msgbox('输入符合要求，谢谢!')
            sys.exit()            
