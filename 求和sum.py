a = [42, 42, 42, 42, 36.11, 34.79, 33.69, 36.6, 'b', True]
sum = 0
for each in a:
	if (type(each) == int) or (type(each) == float):
		sum += each
print(sum)
