# 我的递归的做法
def get(x):
	k = []
	if x:
		k.append(x%10)
		return get(x//10) + k
	else:
		return k
		
t = int(input('input a number:'))
print(get(t))

