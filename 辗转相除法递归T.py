#老师的递归算法:
def gcd(x, y):
	if y:
		return gcd(y, x%y)
	else:
		return x
