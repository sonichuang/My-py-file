class Nstr(str):#我在这个例子中用了字符串拆分的方法，小甲鱼用了字符串的切片的方法来分离空格之前的字符串。
    def __new__(cls, arg = ''): #要对字符串进行长短判断，并且只要空格以前的字符，必须要重写__new__, 因为这个类是继承字符串这个不可变类型。
        if isinstance(arg, str) and arg: #只要参数是字符串，并且不为空
            a = arg.split(maxsplit = 1)#以默认的空格为分隔标志，只分割一次
            arg = len(a [0]) #得到需要的字符串并把它的长度赋给参数 
            return str.__new__(cls, arg) #但是要注意，因为这个类继承了str,所以返回的对象是字符串，这里是字符串长度的字符串。
        else:
            print('Arguments\' type is wrong, must be string and length must at least one.')

    def __lt__(self, other):
        return int(self) < int(other) #所以这里需要转化为整型
    def __le__(self, other):
        return int(self) <= int(other)
    def __eq__(self, other):
        return int(self)  == int(other)
    def __ne__(self, other):
        return int(self) != int(other)
    def __gt__(self, other):
        return int(self) > int(other)
    def __ge__(self, other):
        return int(self) >= int(other)
