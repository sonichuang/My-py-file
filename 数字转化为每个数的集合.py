#迭代的做法
def get(x):
	lt = []
	m = str(x)
	l = len(m)
	for i in range(l):
		t = m[i]
		lt.append(int(t)) # append只能作用在集合里 
	return lt

k = input('input a number:')
print(get(k))


