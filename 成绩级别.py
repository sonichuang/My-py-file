while 1:
    temp = input ('please input your score:')
    grade = int (temp)
    if 90 <= grade < 100:
        print ('The grade is A')
    elif 80 <= grade < 90:
        print ('The grade is B')
    elif 60 <= grade < 80:
        print ('The grade is C')
    elif 0 <= grade < 60:
        print ('The grade is D')
    else:
        print ('Input is wrong!')
        
        
