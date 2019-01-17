#递归的算法 我的思路:
def f(n, x):#n表示有多少人，c表示最后一个人的年龄
	if n == 1:
		return x
	else:
		return f(n - 1, x + 2)

print(f(5,10))

