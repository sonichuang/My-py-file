print('|--- WELCOM ---|')
print('|--- 1：Find the contact  ---|')
print('|--- 2：Add new contact  ---|')
print('|--- 3：Delet contact  ---|')
print('|--- 4：Exit  ---|')
contact = {}
while 1:
	no = int(input('Input the NO.you choose:'))#input输入的都是字符串
	if no == 2:
		name = input('Input the name:')
		if name in contact:
			print('Exsit, the NO of %s is: %d ' % (name, int(contact[name])))
			change = input('Do you want to change the info?(Yes/No):')
			if change == 'Yes':
				NO = int(input('Input the new contact NO:'))
				contact[name] = NO
			else:
				NO = int(contact[name])
				print('NO.: %d' % NO)
		else:
			NO = input('Input the contact NO:')
			contact[name] = NO
	if no == 1:
		name = input('Input the name:')
		if name in contact:
			NO = int(contact[name])
			print('NO.: %d' % NO)
		else:
			print('This name isn\'t in the contacts!')
	if no == 4:
		print('Break down.')
		break
	if no == 3:
		name = input('Input the name:')
		if name in contact:
			del(contact[name])
		else:
			print('This name isn\'t exist in the contact.')
			
			
    
	
