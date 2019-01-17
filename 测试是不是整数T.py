def int_input():
    while True:
        m = input('Please input a integer:')
        if m.isdigit() == False:
            print('It\'s not integer, please input again.')
        else:
            break

int_input()
