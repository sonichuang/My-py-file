'''读取网站信息并保存在对应的文件里。老师的方法与我的相似，不同之处，读取网站信息时使用了分割换行符的方法'''
import urllib.request
import chardet

def main():
    i = 0
    
    with open("urls.txt", "r") as f:
        # 读取待访问的网址
        # 由于urls.txt每一行一个URL
        # 所以按换行符'\n'分割
        urls = f.read().splitlines()
        
    for each_url in urls:
        response = urllib.request.urlopen(each_url)
        html = response.read()

        # 识别网页编码
        encode = chardet.detect(html)['encoding']
        if encode == 'GB2312':
            encode = 'GBK'
        
        i += 1
        filename = "url_%d.txt" % i #老师用了格式化，我用了join的方法

        with open(filename, "w", encoding=encode) as each_file:
            each_file.write(html.decode(encode, "ignore")) #decode的第二个参数。对于有些字符的特殊编码方式，我们可以通过这个方式进行忽略。

if __name__ == "__main__":
    main()
