import urllib.request as ur
import chardet as ch
def source():
    url = input('Please input the URL you want to detect: ')
    try:
        content = ur.urlopen(url).read()
    except:
        print('The URL is wrong or it\'s not available.')
    else:
        return content

def detect():
    try:
        sources = source()
        result = ch.detect(sources)
    except:
        print('You should restart the application again.')
    else:
        result = result['encoding']
        if result == 'GB2312':
            result = 'GBK'
        print('The encoding way is %s.' % result)

if __name__ == '__main__':
    detect()
