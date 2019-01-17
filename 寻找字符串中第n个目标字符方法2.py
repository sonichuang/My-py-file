#寻找长字符串中n个目标字符串的方法2
#如下方法的思路是，通过改变字符串split方法的第二个参数后的结果来计算字符串的索引值
def findStr(string, subStr):
    times = 1
    location = []
    while times:
        listStr = string.split(subStr, times) 
        if len(listStr) <= times:#如果有找到目标字符串的话，得到的listStr的长度等于拆分的次数times加上1
            break               #当所有位置已经找完，再增加times的数值，拆分的结果是不会有改变的
                                #所以当len(listStr) = times 开始就停止循环
        else:
            loc = len(string) - len(listStr[-1]) - len(subStr)
            location.append(loc)
            times += 1
    print(location)

string = "jidajfdua9f[dajfe9fjdjfejfjds"
subStr = "j"
findStr(string, subStr)





