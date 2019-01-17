def f(n):
	if n == 1 or n == 2:
		return 1
	else:
		return f(n1) + f(n-2)
print(f(n))

def f(n):
	n1 = 1
	n2 = 1
	n3 = 1
	while n > 2:
		n3 = n1 + n2
		n1 = n2
		n2 = n3
		n -= 1
	return n3
