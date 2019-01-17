print ('.......................Sonic Huang............................')
while 1 == 1:
    temp = input ('Input a year请输入年份:')
    if not temp.isdigit():
        print ('Please input the int.请输入整数。')
    else:
        year = int (temp)
        if (year%4 ==0) and (year%100 != 0) or (year%400 ==0) :
            print (year,'is leap-year是闰年.')
        else :
            print (year,'is not leap-year不是闰年.')

 
