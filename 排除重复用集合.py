n =[1, 2, 3, 4, 3, 2, 6, 7, 2, 1, 5, 7, 3]
temp = n[:]
n.clear()
for i in temp:
    if i not in n:
        n.append(i)
n.sort()
        
    
