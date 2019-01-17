n = '''string2''' #见第20课课后习题动手1 我的思路是按照题的要求，符合这个要求的时候，把密码小写字母打印出来，第一个字母的索引值m要小于等于l - 9, 当等于的时候说明所有字母已经判断完毕跳出程序
m = 0
l = len(n)
while 1:
	if n[m].islower() and n[m+1].isupper() and n[m+2].isupper() and n[m+3].isupper() and n[m+4].islower() and n[m+5].isupper() and n[m+6].isupper() and n[m+7].isupper() and n[m+8].islower():
		print(n[m+4], end='' )
	if m <= l - 9:
		m += 1
	else:
		break
