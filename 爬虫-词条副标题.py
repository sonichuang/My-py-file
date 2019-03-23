'''本代码通过输入关键字，爬取百度百科该关键字网页上的解释和其他词条以及对应的副标题'''
import requests
from bs4 import BeautifulSoup
import chardet
import re
import urllib.parse as up

#定义一个函数返回目标网页的文本数据
def  ht(url):
    agent = 'User-Agent'
    agentvalue = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    headers = {agent:agentvalue}
    proxy = {'http':'120.78.174.170:8080'}

    response = requests.get(url = url, headers = headers, proxies = proxy)
    code = chardet.detect(response.content)['encoding']#response.content是返回响应的二进制数据
    response.encoding = code #response.encoding可以查询编码方式，也可以通过赋值对响应进行编码
    html = response.text #response.text返回响应的文本数据
    return html

#输入关键字查询
keyword = input('输入关键字查询：')
url = ''.join(['http://baike.baidu.com/search/word?word=', up.quote(keyword)])#对关键字进行编码
html = ht(url)
soup = BeautifulSoup(html, 'html.parser')

list1 = soup.find_all('p') #在关键字没有被收录的页面，搜索结果出现在第一个p便签里面
if '百度百科尚未收录词条' in list1[0].text:
    print(list1[0].text)
else:
    list0 = soup.find_all('meta', attrs={'name':'description'}) #找到对关键字的解释内容,meta标签，含有name='description'的属性和属性值
    description = list0[0]['content']
    print(description)
    print('下面是相关链接：')
    time = 0 #每次显示十行，再询问是否要继续
    for tag in  soup.find_all(href = re.compile('item')):#找到所有包含item属性的标签，所有含有href属性，属性值含有item字符串的标签
        url = ''.join(['http://baike.baidu.com', up.unquote(tag['href'])])
        subhtml = ht(url)
        subsoup = BeautifulSoup(subhtml, 'html.parser')
        subtitle = subsoup.title.string.replace('_百度百科', '')#打开词条链接并找到词条的title文本，title标签
        if '（' in subtitle: #如果词条含有副标题
            print(subtitle, '-->', ''.join(['http://baike.baidu.com', up.unquote(tag['href'])]))
        else:
            print(tag.text, '-->', ''.join(['http://baike.baidu.com', up.unquote(tag['href'])]))
        time += 1
        if time == 10:
            answer = input('退出请回复: n， 其他任意键继续。请输入：')
            if answer == 'n':
                break
            else:
                time = 0
                continue
