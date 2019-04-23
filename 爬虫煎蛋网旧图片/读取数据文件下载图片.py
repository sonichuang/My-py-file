import requests
import chardet
from bs4 import BeautifulSoup
import os.path
import os
import pickle


#定义函数返回地址二进制数据内容
def bhtml(url):
    agent = 'User-Agent'
    agentvalue = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    headers = {agent:agentvalue}
    #proxy = {'http':'120.78.174.170:8080'} , proxies=proxy    
    response = requests.get(url=url, headers=headers, timeout = 5)
    bhtml = response.content
    return bhtml



#页面所有图片的地址列表
def getpicurl(soup):
    list1 = soup.find_all('img')
    for eachurl in list1:
        picurl = eachurl['src']
        yield picurl

#从allurl.txt读取数据并下载图片        
def main():
    try:#新建一个文件夹，如果已经存在就pass
        os.mkdir('D:\download\pic')
    except:
        pass
    os.chdir(r'D:\download\pic') #改变工作目录

    #如果第一次运行，就直接从allurl.txt读取数据, passurl和okurl都为空。
    #如果中途因为各种原因停止了程序，那么从allurl中删除已经下载的和没有下载成功的地址，这样可以避免重启时重复下载图片。
    try:
        with open(r'D:\download\pic\passurl.txt', 'rb') as psurl:
            passurllist = pickle.load(psurl)
        with open(r'D:\download\pic\okurl.txt', 'rb') as goodurl:
            okurllist = pickle.load(goodurl)
        with open(r'D:\download\pic\allurl.txt', 'rb') as totalurl:
            allurllist = pickle.load(totalurl)
    except:
        passurllist = []
        okurllist = []
        with open(r'D:\download\pic\allurl.txt', 'rb') as totalurl:
            allurllist = pickle.load(totalurl)
    else:
        newalllist = [x for x in allurllist if x not in passurllist and x not in okurllist]
        with open(r'D:\download\pic\allurl.txt', 'wb') as total:
            pickle.dump(newalllist, total)
    #遇到读取数据时出现问题就把地址保存在passurl里面，下载完成的保存在okurl里面。
    for eachpicurl in allurllist:
        picname = os.path.split(eachpicurl)[1]
        try:
            picdata = bhtml(eachpicurl)
        except:
            print(eachpicurl, '下载有问题')
            passurllist.append(eachpicurl)
            with open('passurl.txt', 'wb') as f1:
                pickle.dump(passurllist, f1)
            continue
        else:
            try:
                with open(picname, 'wb') as f:
                    f.write(picdata)
            except:
                print(eachpicurl, '下载有问题')
                passurllist.append(eachpicurl)
                with open('passurl.txt', 'wb') as f4:
                    pickle.dump(passurllist, f4)
                continue
            else: 
                print(eachpicurl, '下载ok')
                okurllist.append(eachpicurl)
                with open('okurl.txt', 'wb') as f3:
                    pickle.dump(okurllist, f3)

if __name__ == '__main__':
    main()
