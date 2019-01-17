#我的做法 通过不断给a和b赋值，直到d=0
def power(a, b):
	a1 = a
	b1 = b
	while (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
		c = a // b
		d = a % b
		if d == 0:
			print('(', a1, ',', b1, ')', '=', b )
			break
		else:
			a = b
			b = d
