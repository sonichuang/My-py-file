'''此脚本通过读取urls.txt上的网站的信息，并保存在对应的文本文件里。'''
import urllib.request as ur
import chardet as ch

def main():
    with open('urls.txt') as file:
        urls = file.readlines()#分行读取
        n = 0
        for url in urls:
            sources = ur.urlopen(url).read()
            code = ch.detect(sources)['encoding']#检测网站的编码方式
            html = sources.decode(code)#对网站信息进行相应的解码,decode默认的是encoding = 'utf-8'的编码
            n += 1
            filename = ''.join(['file_', str(n), '.txt'])#生成对应的文件
            with open(filename, 'w', encoding = code) as nfile:#再用相应的编码写入对应的文件，encoding默认的编码是utf-8
                nfile.write(html)

if __name__ == '__main__':
    main()
        
        
