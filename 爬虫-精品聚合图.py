import requests
from bs4 import BeautifulSoup
import chardet
import os.path
import os
import time
import pickle

#定义函数返回地址二进制数据内容
def bhtml(url):
    agent = 'User-Agent'
    agentvalue = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    headers = {agent:agentvalue}
    #proxy = {'http':'120.78.174.170:8080'} , proxies=proxy    
    response = requests.get(url=url, headers=headers)
    bhtml = response.content
    return bhtml
    
#每个地址的soup数据   
def  data(url):
    agent = 'User-Agent'
    agentvalue = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    headers = {agent:agentvalue}
    #proxy = {'http':'120.78.174.170:8080'} , proxies=proxy
    
    response = requests.get(url=url, headers=headers)
    global code
    code = chardet.detect(response.content)['encoding']
    response.encoding = code
    html = response.text
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

    
#所有分页的地址(生成器)
def getpage():
    page = 12
    for n in range(page, 0, -1):#页面倒数到1
        pageurl = ''.join(['http://www.jingpinjuhe.com/?cat=26&paged=', str(n)])
        yield pageurl


#所有分页的地址(生成器)
def getitempage(soup):
    list1 = soup.find_all('a', attrs={'target':'_blank', 'title':True})  # <a target="_blank" href="url address" title="title message">some message</a> 
    for eachitem in list1:
        itemurl = eachitem['href']
        itemtitle = eachitem['title']
        print(itemtitle, itemurl, '下载中....')
        yield itemurl


#每个页面的图片地址，下载保存到本地, 
def downpic(soup):
    passurllist = []
    list2 = soup.find_all('img', attrs={'src':True})
    for pictag in list2:
        eachpicurl = pictag['src']
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
        if eachpicurl in ['http://www.jingpinjuhe.com/wp-content/themes/xiu/images/logo.png']:#如果是网站图标则忽略
            continue
        picname = os.path.split(eachpicurl)[1]
        try:
            #导出图片的二进制数据
            picdata = bhtml(eachpicurl)
        except:
            print(eachpicurl, '下载有问题')
            passurllist.append(eachpicurl)
            with open('passurl.txt', 'wb') as f1:
                pickle.dump(passurllist, f1)            
            continue
        else:
            if 'gif' not in picname:#不下载gif图片
                with open(picname, 'wb') as f:
                          f.write(picdata)
                time.sleep(0.5)

def main():
    try:#新建一个文件夹，如果已经存在就pass
        os.mkdir(r'D:\download\pic\new')
    except:
        pass
    os.chdir(r'D:\download\pic\new') #改变工作目录
    url = r'http://www.jingpinjuhe.com/?cat=26&paged=12' #最后一页
    pageurl = getpage()#所有页码的地址
    for x in  pageurl:
        print(x)
        pagesoup = data(x)#每个页面的soup
        itemaddress = getitempage(pagesoup)
        for itemurl in itemaddress:
            if itemurl in [r'http://www.jingpinjuhe.com/?p=2965']:
                continue
            itemsoup = data(itemurl)
            downpic(itemsoup)
        print('下载完毕.')
            


if __name__ == '__main__':
    main()
                  
        
