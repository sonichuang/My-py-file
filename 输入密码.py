i = 3
while i:
    code = input('input your code:')
    if '*' in code:
        print("can't have * in code, you still have", i, "chance left", "please input code:", end="")
        continue
    elif code == 'sonichuang':
        print('code is correct.')
        break
    else:
        print('code is wrong, you still have', i-1, 'chance left,', end="")
    i -= 1
    

