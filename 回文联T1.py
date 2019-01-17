#老师讲的:一句话的左边第一个字(索引值为range(length//2))和右边第一个字(索引值为length-1)的比较，再比较第二个字，比较length//2 次
def palindrome(string):
	length = len(string) #一句话的长度
	last = length-1 #右边第一个字的索引值
	length //= 2 #比较的次数
	flag = 1
	for each in range(length):
		if string[each] != string[last]:
			flag = 0
	last -= 1
#上面的循环是连续比较如果不相等flag = 0
	if flag == 1:
		return 1
	else:
		return 0

string = input('请输入一句话：')
if palindrome(string) == 1:
	print('是回文联!')
else:
	print('不是回文联！')
	


