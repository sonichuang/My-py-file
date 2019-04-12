import requests
import re
from bs4 import BeautifulSoup
import chardet
import urllib.parse as up
import base64
import os.path
import os
import time
import pickle

#自定义一个异常类
class Stopdownload(Exception):
    def __init__(self, err='遇到旧图片,停止下载了。'):
        Exception.__init__(self, err)


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
    soup = BeautifulSoup(html, 'html.parser')
    return soup

    
#所有分页的地址(生成器)
def getpage(soup):
    list1 = soup.find_all('span', attrs={'class':'current-comment-page'})  # <span class="current-comment-page">[56]</span>
    a = list1[0].text #a='[56]'他是一个字符串
    page = int(a[1:3]) #切片
    
    for n in range(page-1, 0, -1):#页面倒数到1
        pageurl = ''.join(['http://jandan.net/ooxx/page-', str(n), '#comments'])
        yield pageurl

#每个页面的图片地址，下载保存到本地, 
def downpic(soup):
    try: #打开保存的已下载的图片名数据
        with open('D:\download\piclist.txt', 'rb') as f2:
            list1 = pickle.load(f2)#把数据导入列表1
    except: #如果第一次下载，列表1为空列表
        list1 = []
    #找到包含有页面图片下载地址的标签列表2
    #list2 = soup.find_all('span', attrs={'class':'img-hash'}) #网站使用了反爬机制，参考https://www.jianshu.com/p/5351baf254ef
    list2 = soup.find_all('a', attrs={'class':'view_img_link'})
    #定义一个空的列表3
    list3 = []
    #找到所有图片的下载地址和图片名称
    for eachcode in list2:
        #piccode = str(base64.b64decode(eachcode.string.encode(code)))[2:].replace('mw600', 'large').replace('\'', '')#网站使用反爬机制，需要对数据进行解密。参考https://www.jianshu.com/p/5351baf254ef
        piccode = eachcode['href']
        picurl = ''.join(['http:', piccode])
        if picurl in ['http://ww3.sinaimg.cn/large/006XNEY7gy1g1xabxlnq4j30fo0jwwhv.jpg']:#如果网页的图片出现的加载错误，导致不能读取picdata。就需要跳过这个图片。其实也可以使用异常处理的方法
            continue
        picname = os.path.split(picurl)[1]
        #导出图片的二进制数据
        picdata = bhtml(picurl)
        #如果图片没有下载过，则下载图片, 并把图片名导入列表3
        if picname not in list1:
            print(picname)
            list3.append(picname)
            with open(r'D:\download\temp.txt', 'ab') as f3:#把列表3的数据保存在临时文件(包括新下载的图片名)
                pickle.dump(list3, f3)

            if 'gif' not in picname:#不下载gif图片
                with open(picname, 'wb') as f:
                          f.write(picdata)
                time.sleep(0.5)
        else:#如果有下载过
            print(picname, '是旧图片')
            list3.append(picname)
            with open(r'D:\download\temp.txt', 'ab') as f3:
                pickle.dump(list3, f3)
            raise Stopdownload() #抛出异常

def main():
    try:#新建一个文件夹，如果已经存在就pass
        os.mkdir('D:\download\pic')
    except:
        pass
    os.chdir(r'D:\download\pic') #改变工作目录
    mainurl = 'http://jandan.net/ooxx' #主页
    print(mainurl)
    mainsoup = data(mainurl)#导出主页的soup
    try:
        downpic(mainsoup)#下载主页的图片，如果全部是新图片不会触发异常
    except Stopdownload as e:#如果遇到旧图片则停止下载
        print(e)
        pass
    else:#如果没有遇到旧图片
        pageurl = getpage(mainsoup)#下面页码的地址
        for x in  pageurl:
            print(x)
            pagesoup = data(x)#每个页面的soup
            try:
                downpic(pagesoup) #下载每个页面的图片
            except Stopdownload as e:#如果遇到旧图片立刻停止循环
                print(e)
                break
    #删除旧的文件数据，把临时文件改为正式文件，储存了最新下载的图片名数据
    
    os.remove(r'D:\download\piclist.txt')
    os.rename(r'D:\download\temp.txt', r'D:\download\piclist.txt')

#为了是在下载图片时遇到旧图片时停止下载，而不用继续循环读取旧页面的数据，
#我在下载图片的函数中使用raise语句，当出现旧图片时立刻引发异常。
#在主函数中就可以捕获这个异常而中断循环。

if __name__ == '__main__':
    main()
                  
        
