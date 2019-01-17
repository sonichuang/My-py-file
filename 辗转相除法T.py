#老师的做法	循环赋值，到y=0,为Faulse为止	
def gcd(x, y):
	while y:
		t = x % y
		x = y
		y = t
	return x
	

		




