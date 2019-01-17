a = 0
while a >= 0 and a <= 1000:
	n = 0
	A = list(str(a))
	while A:
		n += (int(A.pop()))**3
	if a == n:
		print(a)
	a += 1


	
	
