#我的思路:通过比较原字符串与倒转的字符串是否一样
def fun():
	rword = []
	word = input('imput a words:')#输入一个字符串
	lword = list(word)#把字符串每个字符转化成一个列表
	Lword = tuple(lword)#把列表转化为元组，因为把原始字符串转化为元组后就不能被修改，不会受后面pop()对列表的影响
	while lword:
		rword += lword.pop()#把原始字符串的列表从后往前一个字符一个字符叠加进一个空的列表，然后组成新的列表
	Rword = tuple(rword)#把新的列表转化为元组
	if Rword == Lword:#比较两个元组
		print('that\'s what we want.')
	else:
		print('that\'s not we want.')
		



