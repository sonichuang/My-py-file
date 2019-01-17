def recursion(x):
	if x == 1:
		return 1
	else:
		return x * recursion(x-1)
		
y = int(input('input a number:'))
r = recursion(y)
print('Recursion of %d is %d.' % (y, r))
