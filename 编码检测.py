'''本脚本是利用文本编码检测工具chardet检测用户输入的网站所使用的编码。'''
import urllib.request as ur
import chardet as ch

#定义一个函数用于接收网站数据
def source():
    url = input('Please input the URL you want to detect: ')
    try:#检测用户输入的网址是否正确
        content = ur.urlopen(url).read()
    except:
        print('The URL is wrong or it\'s not available.')
    else:
        return content

#检测网站的编码
def detect():
    try:#如果用户输入的网址有问题这里就会抛出异常，为了使脚本运行正常，这里进行了处理，并提示用户。
        sources = source()
        result = ch.detect(sources)
    except:
        print('You should restart the application again.')
    else:
        result = result['encoding']
        if result == 'GB2312': #参考https://www.zhihu.com/question/19677619
            result = 'GBK'
        print('The encoding way is %s.' % result)

#如果作为单独脚本运行时
if __name__ == '__main__':
    detect()
