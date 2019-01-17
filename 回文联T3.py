# 老师的递归算法:利用递归每次索引前后两个字符进行对比，当start > end的时候，也正是首尾下标“碰面”的时候，即作为结束递归的条件。
def is_palindrome(n, start, end):
	if start > end:#start数值从0不断加1，end数值从最大的索引值不断减1，直到start值等于end比较完毕
		return 1     
	else:
		return is_palindrome(n, start+1, end-1) if n[start] == n[end] else 0 # 返回中的条件判断做法

string = input('请输入一串字符串：')
length = len(string)-1

if is_palindrome(string, 0, length):
	print('\"%s\"是回文字符串!' % string) #如果返回1。 格式化字符串
else: # 如果返回0
	print('\"%s\"不是回文字符串!' % string)
