#寻找一个长字符串里面若干个目标字符串的位置的方法
#如下方法的思路是，通过改变字符串find方法的起始位置重复找到所有的位置
#当所有位置已经找完，后面再没有发现目标字符串的时候find方法会返回一个-1值，这样就可以退出循环
def findindex(str, substr):
    count = 1    #给count赋值为1是为了可以让循环体工作
    indexlist = []
    while count:
        if count == 1:
            index = str.find(substr) #先找到默认的第一个位置
            count += 1
        else:
            index = str.find(substr, index+1) #然后从第一个位置后面一个位置开始查找，再循查找，直到返回-1值
            if index == -1:
                break
        indexlist.append(index)#最后找到的每个位置，写入列表
    print(indexlist)

str = 'jidajfdua9f[dajfe9fjdjfejfjds'
substr = 'j'
findindex(str, substr)
