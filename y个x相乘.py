#我的做法 简单粗暴
def power(x, y):
	if (type(x) == int) or (type(x) == float) and (type(y) == int) or (type(y) == float):
		return (x**y)

	
#我的递归算法:
def power(x, y):
	if y == 0:
		return 1
	else:
		return x * power(x, y - 1)


