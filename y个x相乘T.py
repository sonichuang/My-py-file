#老师的做法:y个x叠加相乘
def power(x, y):
	result = 1
	for i in range(y):
		result *= x
	return result
		
# 老师的递归算法:
def power(x, y):
	if y:
		return x * power(x, y-1)
	else:
		return 1
