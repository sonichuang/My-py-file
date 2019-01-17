def countthem():
	n = input('input string:')
	countD = 0
	countA = 0
	countS = 0
	countE = 0
	for i in n:
		if i.isdigit():
			countD += 1
		elif i.isalpha():
			countA += 1
		elif i.isspace():
			countS += 1
		else:
			countE += 1
	print('have %d numbers, %d alphabets, %d spaces, %d Else' % (countD, countA, countS, countE))
	
	
