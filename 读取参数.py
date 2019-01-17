class Ca:#*args是指任意个无名参数，他是一个参宿为元素的元组，可以是数字，字符串，None. **kwargs是值任意个关键字参数，他是一个由参数名为key,参数值为value组成的dict.
    def __init__(self, *args):
        if not args:
            print('Haven\'t inserted any arguments')
        else:
            print('Have inserted %d arguments, they are:' % len(args), end = '')
            for i in args:
                print(i, '', end = '')


            

        
