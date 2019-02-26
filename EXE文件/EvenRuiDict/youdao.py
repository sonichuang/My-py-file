import urllib.request as ur
import urllib.parse as up
import time
import random
import hashlib
import json
def translate(content):
    #请求的地址：
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    #表单数据关键数据ts, salt, sign的计算方法
    client = 'fanyideskweb'
    ts = int(time.time() * 1000) 
    num = random.randint(1, 10)#从1到10的随机数
    salt = str(ts) + str(num)
    flowerStr = 'p09@Bn{h02_BIEe]$P^nG'
    sign = hashlib.md5((client + content + salt + flowerStr).encode('utf-8')).hexdigest()
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = client
    data['salt'] = salt #salt的值可以是时间戳和随机数数值相加的结果，也可以是对应字符串相加的结果。可以是int,也可以是str
    data['sign'] = sign#sign的值是client(固定值),content(变化值),salt(变化值),固定字符串拼接后的md5值
    data['ts'] = ts #ts的值是一个时间戳，可以是int也可以是str
    data['bv'] = '3e6546407cd5c219c8baa670735759b6' #bv是浏览器和版本信息的md5值
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    #解析表单数据并编码
    data = up.urlencode(data).encode('utf-8')
    #下面的header数据需要填入,并实例化
    req = ur.Request(url = url, data = data, method = 'POST')   
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36')
    req.add_header('Referer', 'http://fanyi.youdao.com/')
    req.add_header('Cookie', 'OUTFOX_SEARCH_USER_ID=602357771@10.169.0.84')
#处理网络问题异常
    try:
        #请求并接受反馈信息, timeout是以秒单位确定连接的超时时间
        response = ur.urlopen(req, timeout = 5)
    except: #提示错误
        result = 'Error! Check your connection. 出问题了, 请检查网络连接.'
        return result
    else:
        #读取反馈信息并解码
        html = response.read().decode('utf-8')
        #利用json库把json数据转化为python的列表或者字典
        result = json.loads(html)['translateResult'][0][0]['tgt']
        return result

if __name__ == '__main__':
    #需要翻译的内容：
    content = input('Input what you want to translate:')
    res = translate(content)
    print('The result is ==>> %s.' % res)


              
