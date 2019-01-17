#老师的第二个方法:用reversed()
def palindrome(string):
	list1 = list(string)#把字符串转化为列表
	list2 = reversed(list1)#
	if list1 == list(list2):
		return '是回文联!'
	else:
		return 
		'不是回文联！'
print(palindrome('上海自来水来自海上'))


