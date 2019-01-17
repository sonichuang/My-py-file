#根据老师的程序改变改进了程序:
count = {}		
def new():
	while 2:
		name = input('Input the name:')
		if name in count:
			print('Already Exist, input again')
			continue
		else:
			password = input('input the password:')
			count[name] = password
			break
			
def old():#特别要注意下面的程序设计，根据老师上面的那段chosen = False的代码的启发。
	choose = False #这里的赋值是为了通过对变量来控制循环的运行
	while not choose:#这里实际上就是while True
		name = input('Input the name:')
		if name in count:
			while 2:
				password = input('input the password:')
				if password == count[name]:
					print('Welcom to the system!')
					choose = True #这里要这样赋值是为了，当显示Welcom to the system!后跳出while not choose的循环
					break #跳出while 2的循环
					
				else: 
					print('Password is wrong,please input again:')
		else:
			print('This name isn\'t exist, input the name again')
			
def menu():
	while 1:
		print('-----------')
		print('NEW: N/n')
		print('LOGIN: E/e')
		print('EXIT: Q/q')
		print('-----------')
		order = input('input the order:')
		if order == 'N' or order == 'n':
			new()
		if order == 'E' or order == 'e':
			old()
		if order == 'Q' or order == 'q':
			break
		if order not in 'NEQneq':
			print('Input the order again.')
			
menu()

