name = input('input the file name:')
f = open(name, 'a')
print('input the content:')
while 1:
    content = input()
    if content != 'close':
        f.write('%s\n' % content)#这里注意接受每次输入后换行
    else:
        f.close()
        break
 
    
         
