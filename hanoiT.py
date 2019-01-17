def hanoi(n, x, y, z):
	if n == 1:
		print(x, '-->', z)
	else:
		hanoi(n-1, x, z, y) #将n-1个盘子从x借助z移动到y
		print(x, '-->', z)
		hanoi(n-1, y, x, z) #将n-1个盘子从y借助x移动到z
		
n = int(input('请输入层数:'))
hanoi(n, 'x', 'y', 'z')

		
