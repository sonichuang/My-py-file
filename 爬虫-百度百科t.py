import requests
from bs4 import BeautifulSoup
import chardet
import re
import urllib.parse as up

url = 'http://baike.baidu.com/view/284853.htm'
agent = 'User-Agent'
agentvalue = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
headers = {agent:agentvalue}
proxy = {'http':'120.78.174.170:8080'}

response = requests.get(url = url, headers = headers, proxies = proxy)
code = chardet.detect(response.content)['encoding']#response.content是返回响应的文本数据
response.encoding = code #response.encoding可以查询编码方式，也可以通过赋值对响应进行编码
html = response.text #response.text返回响应的二进制数据
soup = BeautifulSoup(html, 'html.parser')
for tag in  soup.find_all(href = re.compile('item')):
    print(tag.text, '-->', ''.join(['http://baike.baidu.com', up.unquote(tag['href'])]))
