def findSubstring(string,substring,times):
    current = 0
    for i in range(1,times+1):
        current = string.find(substring,current)+1
        if current == 0 :  return -1

    return current-1


