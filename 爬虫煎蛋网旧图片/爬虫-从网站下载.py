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

#主程序会生成一个包含有所有图片下载地址的allurl.txt的二进制文件
def main():        
    allurllist = []
    try:#新建一个文件夹，如果已经存在就pass
        os.mkdir('D:\download\pic')
    except:
        pass
    os.chdir(r'D:\download\pic') #改变工作目录

    url = r'http://js.funet8.com/html/jiandan-meizhi.html' #网站地址
    soupdata = data(url) #网站的soup数据
    pictureurl = getpicurl(soupdata) #生成器产生的每张图片的地址
    for eachpicurl in pictureurl:
        #对地址进行删选。由于网页代码的一些问题，导致地址出现一些错误
        if '<img src=' in eachpicurl:
            continue
        if ' />' in eachpicurl:
            eachpicurl = eachpicurl.replace(' />', '')
        #修改一下可以得到大图的地址
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
        #把所有地址组成的列表写入文件
        allurllist.append(eachpicurl)
        with open('allurl.txt', 'wb') as f2:
            pickle.dump(allurllist, f2)


if __name__ == '__main__':
    main()
