def n(x):
    temp = x[:]
    x.clear()
    for i in temp:
        if i not in x:
            x.append(i)
    x.sort()
    print(x)
        
  
