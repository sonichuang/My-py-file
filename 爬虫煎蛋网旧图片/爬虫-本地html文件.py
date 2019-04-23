import requests
import chardet
from bs4 import BeautifulSoup
import os
import pickle




#页面的soup数据
def  data(url):
    agent = 'User-Agent'
    agentvalue = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    headers = {agent:agentvalue}
    #proxy = {'http':'120.78.174.170:8080'} , proxies=proxy
    
    response = requests.get(url=url, headers=headers, timeout = 5)
    global code
    code = chardet.detect(response.content)['encoding']
    response.encoding = code
    html = response.text
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

#页面所有图片的地址列表
def getpicurl(soup):
    list1 = soup.find_all('img')
    for eachurl in list1:
        picurl = eachurl['src']
        yield picurl
        

def main():
    allurllist = []

    try:#新建一个文件夹，如果已经存在就pass
        os.mkdir('D:\download\pic')
    except:
        pass
    os.chdir(r'D:\download\pic') #改变工作目录

    url = r'E:\python files\IDEL FILES\My py file\爬虫煎蛋网旧图片\jiandan.html' #文件保存地址，需要根据实际情况变化

    #读取本地html文件，注意open的参数需要加上encoding的参数，否则会出现编码错误，至于编码方法可以用chardet测试
    #得到的f是一个迭代器，迭代出的是包含每个图片地址标签的字符串，如果我们直接对这个标签字符串进行操作会很麻烦，所以用BeautifulSoup进行解析
    with open(url, mode='r', encoding='utf-8') as f:
        soupdata = BeautifulSoup(f, 'html.parser')
    pictureurl = getpicurl(soupdata)
    for eachpicurl in pictureurl:
        if '<img src=' in eachpicurl:
            continue
        if ' />' in eachpicurl:
            eachpicurl = eachpicurl.replace(' />', '')
        if 'sinaimg' in eachpicurl:
            if 'bmiddle' in eachpicurl:
                eachpicurl = eachpicurl.replace('bmiddle', 'large')
            if 'mw690' in eachpicurl:
                eachpicurl = eachpicurl.replace('mw690', 'large')
            if 'mw600' in eachpicurl:
                eachpicurl = eachpicurl.replace('mw600', 'large')
            if 'thumbnail' in eachpicurl:
                eachpicurl = eachpicurl.replace('thumbnail', 'large')
            if 'small' in eachpicurl:
                eachpicurl = eachpicurl.replace('small', 'large')
            if 'thumb150' in eachpicurl:
                eachpicurl = eachpicurl.replace('thumb150', 'large')
        allurllist.append(eachpicurl)
        with open('allurl.txt', 'wb') as f2:
            pickle.dump(allurllist, f2)

if __name__ == '__main__':
    main()

