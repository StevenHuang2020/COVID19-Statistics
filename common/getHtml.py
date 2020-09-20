#python3 unicode
#author:Steven Huang 10/02/20
#function:common get html content by requests
import sys
import requests
import urllib.request
from .headersRandom import userAgentHeaders
from .userAgent import GetUA
import wget      #pip instal wget

def getUrlByUrllib(url):
    try:
        with urllib.request.urlopen(url) as response:
            charset = response.info().get_content_charset()
            print('charset = ', charset)
            if charset == None:
                charset = "utf-8"
            html = response.read().decode(charset, 'ignore')
            return html
    except:
        return "Something Wrong by Urllib!"
        
def getUrlByRequest(url):
    if 0:
        #url = 'https://api.github.com/some/endpoint'
        #headers = {'user-agent': 'my-app/0.0.1'}
        #r = requests.get(url, headers=headers)

        #payload = {'key1': 'value1', 'key2': 'value2'}
        #r = requests.get("http://httpbin.org/get", params=payload)
        headers = userAgentHeaders()
        print(headers)
        r = requests.get(url,headers=headers)
        print(r.status_code)
        return r.text
        
    try:
        if 0:
            headers = requests.utils.default_headers()
            print('headers=',headers)
            headers.update(
            {
            'User-Agent':GetUA()
            })
        
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(r.status_code)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong by requests!"
    
    
def openUrl(url, save=False, file=r'./a.html'):
    print('start to open url:',url)
    html = getUrlByRequest(url)
    if save:
        saveToFile(html,file)
    return html

def saveToFile(html, file):
    with open(file, "w", encoding='utf-8') as text_file:
        text_file.write(html)

def openUrlUrlLib(url,save=False, file=r'./a.html'):
    html = getUrlByUrllib(url)   
    if save:
        saveToFile(html,file)
    return html


def downWebFile(url,dst):
    if 0:
        wget.download(url, out=dst)
    else:
        print('Beginning file download with requests')
        r = requests.get(url)
        # # Retrieve HTTP meta-data
        # print(r.status_code)
        # print(r.headers['content-type'])
        # print(r.encoding)
        with open(dst, 'wb') as f:
            f.write(r.content)
