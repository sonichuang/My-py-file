al = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nu = '0123456789'
sy = r'''~!@#$%^&*()\_=-/,.?<>;:[]{}|'''
password = input('input your password to check the grade:')
length = len(password)
while (password.isspace() or length == 0):
   password = input('what you input is nothing, please input again:')
   length = len(password)
if length < 8:
    leng = 1
if 8 <= length <= 16:
    leng = 2
if 16 < length:
    leng = 3
con = 0
for each in password:
    if each in al:
        con += 1
        break
for each in password:
    if each in nu:
        con += 1
        break
for each in password:
    if each in sy:
        con += 1
        break
while 1:
    print('the grade is:', end='')
    if (leng == 1) and (con == 1):
        print('low.')
    elif (leng == 3) and (con == 3) and (password[0] in al):
        print('high.')
        print('good job,stick to it.')
        break
    else:
        print('middle.')
    print('''the way to upgrade the password as following:
      1.must have alphabet, number and symbol together.
      2.must begin with the alphabet.
      3.legth can't less than 16.''')
    break
    
