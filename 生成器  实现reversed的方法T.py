def myRev(data):
    # 这里用 range 生成 data 的倒序索引
    # 注意，range 的结束位置是不包含的
    for index in range(len(data)-1, -1, -1):
        yield data[index]


t = myRev('tomorrow morning')
for x in t:
    print(x, end = '')
    
