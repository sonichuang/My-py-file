#我的程序
count = {}
while 1:
	print('-----------')
	print('NEW: N/n')
	print('LOGIN: E/e')
	print('EXIT: Q/q')
	print('-----------')
	order = input('input the order:')
	if order == 'N' or order == 'n':
		name = input('Input the name:')
		while 2:
			if name in count:
				print('Already Exist!')
				name = input('Input again:')
			else:
				password = input('input the password:')
				count[name] = password
				break
	if order == 'E' or order == 'e':
		name = input('Input the name:')
		while 3:
			if name in count:
				password = input('input the password:')
				if password == count[name]:
					print('Welcom to the system!')
					break
				else: 
					print('Password is wrong,please input again:')
			else:
				print('This name isn\'t exist')
				break
	if order == 'Q' or order == 'q':
		break
		
			

