n = 7
i = 0
while i < 1000:
    if (n%2 == 1) and (n%3 == 2) and (n%5 == 4) and (n%6 == 5) and (n%7 == 0):
        flag = 1
        i += 1
    else:
        n += 1
if flag == 1:
    print ('found the number is',n)

        
