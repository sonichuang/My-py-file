#老师思路:先定义一个空的列表list1, 字符串的字符如果没有在列表里，就计算这个字符的个数，然后把他添加在列表里。跟我的思路不一样，我是跳过了字母，最后再显示出来。
str1 = '''拷贝过来的字符串'''
list1 = []

for each in str1:
    if each not in list1:
        if each == '\n':
            print('\\n', str1.count(each))
        else:
            print(each, str1.count(each))
        list1.append(each)
