'''本程序是通过输入联系人和电话号码然后转为为华为手机vcard的vcf文件，vcf文件可以直接上传到华为手机通讯录。'''
import urllib.parse as up
import pickle
import os

'''定义函数返回一个联系人的字典'''
def contacts():
    print('|--- 欢迎进入通讯录 ---|')
    print('|--- 1：查找联系人  ---|')
    print('|--- 2：增加或修改联系人  ---|')
    print('|--- 3：删除联系人  ---|')
    print('|--- 4：显示所有通讯录  ---|')
    print('|--- 5：保存并退出通讯录  ---|')
    
    #从内存中的二进制文件中读取联系人信息
    try:
        with open('contact.txt', 'rb') as f2:
            contact = pickle.load(f2)
    except:#如果内存中没有文件者则赋值为一个空的字典
        contact = {}
        
    while 1:
        no = input('请选择:')#input输入的都是字符串
        #查找联系人
        if no == '1':
            name = input('输入联系人姓名:')
            if name in contact:#联系人存在则打印他的号码
                NO = contact[name]
                print('号码是: %s' % NO)
            else:
                print('联系人不存在!')
        #添加联系人
        if no == '2':
            name = input('输入联系人姓名:')
            if name in contact:#如果联系人已经存在，打印联系电话，并询问是否要修改
                print(' 联系人%s 的电话是: %s ' % (name, contact[name]))
                change = input('修改原号码回复y, 增加号码回复z, 什么都不做回复n:')
                if change == 'y':
                    NO = input('输入新号码\(多个号码请用+连接\):')
                    contact[name] = NO
                elif change == 'z':
                    NO = input('输入号码\(多个号码请用+连接\):')
                    contact[name] += NO
                else:
                    NO = contact[name]
                    print('号码是: %s' % NO)
            else:
                NO = input('输入联系人号码:')
                contact[name] = NO
        #删除联系人      
        if no == '3':
            name = input('输入联系人姓名:')
            if name in contact:
                del(contact[name])
            else:
                print('联系人不存在.')
        #显示所有通讯录     
        if no == '4':
            if contact == {}:
                print('通讯录是空的.')
            else:
                for i in contact:
                    print(i, ':', contact[i])
        #保存并退出          
        if no == '5':
            print('保存并退出.')
            break
        
    #写入一个二进制文件保存数据
    with open('contact.txt', 'wb') as f1:
        pickle.dump(contact, f1)
    return contact #返回字典数据


'''清除之前的通讯录'''
try:
    os.remove('newdata.vcf')
except:
    pass

#华为通讯录vcard代码字符串
info1 = 'BEGIN:VCARD\nVERSION:2.1\nN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;'
info2 = ';;;\nFN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:'
info3 = '\nTEL;CELL:'
info4 = '\nEND:VCARD\n'

#通过输入通讯录后导出联系人的字典数据
allno = contacts()
#把字典数据转化为vcard代码并写入newdata.vcf文件
for i in allno:
    name = i
    #通过列表解析式删除数据里面的空格
    nostr = ''.join([x for x in allno[i] if x != ' '])
    nolist = nostr.split('+') #如果有多个电话号码需要每个电话分离出来组成一个列表
    list2 = []
    for no in nolist:
        #注意vcard电话号码的格式数字之间有空格
        no = no[:3] + ' ' + no[3:7] + ' ' + no[7:]        
        list2 += [info3, no] #每个电话号码会形成单独一行
    name = up.quote(name).replace('%', '=') #vcard联系人的名字是经过url编码后把%换成=
    with open('newdata.vcf', 'a') as file: #把通讯录代码写入vcard
        list1 = [info1, name, info2, name]
        list3 = [info4]
        data = ''.join(list1 + list2 + list3)
        file.write(data)
    

    
                    

    
