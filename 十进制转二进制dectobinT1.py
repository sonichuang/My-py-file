# 老师的递归的做法
		
		
def f(x):
	n = ''
	if x:
		n = f(x//2)
		return n + str(x%2)
	else:
		return n
