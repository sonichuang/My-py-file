'''本代码使用代理ip登录查询ip的网站来验证代理运行是否成功, 以及opener, header的使用'''
import urllib.request as ur
import chardet
#需要登录的网站可以显示当前的ip地址
url = 'http://myip.kkcha.com/'
agent = 'User-Agent'
agentvalue = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
proxy = {'http':'120.78.174.170:8080'}

#前三行定义一个特殊的opener,来使用代理或者其他来方式打开url. 如果没有定义,urlopen就是用默认的方式去打开url.
proxy_support = ur.ProxyHandler(proxy)#handler我的理解就是用什么方法来handle
opener = ur.build_opener(proxy_support)#opener就是生成一个工具


#0 是否安装opener

#ur.install_opener(opener) #安装opener
response = opener.open(url)#如果前一行不安装opener,就用opener来打开url
#response = ur.urlopen(url) #如果已经安装opener, 调用urlopen(url)就会自动用安装的opener的方式来处理

#1 request参数添加header
'''
headers = {agent:agentvalue}
request = ur.Request(url = url, headers = headers)
response = opener.open(request)
'''
#2 opener添加header
'''
opener.addheaders = [(agent, agentvalue)]
response = opener.open(url)
'''

#3 request添加header
'''
request = ur.Request(url)
request.add_header(agent, agentvalue)
response = opener.open(request)
'''

content = response.read()#response.read()运行一次后read的指针就在被读取内容的最后，如果再次调用将返回为空.所以这里把他的值赋值给一个变量
code = chardet.detect(content)['encoding']
html = content.decode(code)
print(html)



