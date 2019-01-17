while 1:
	decimalism = input('Input a integer (input Q to close.):')
	if decimalism =='Q':
		break
	octanary = '%o' % int(decimalism)
	sexadecimal = '%x' % int(decimalism)
	binary = bin(int(decimalism))
	print('Decimalism --> Sexadecimal:', decimalism, '-->', sexadecimal)
	print('Decimalism --> Octanary:', decimalism, '-->', octanary)
	print('Decimalism --> Binary:', decimalism, '-->', binary)
