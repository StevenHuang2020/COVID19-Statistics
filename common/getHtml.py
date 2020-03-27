#python3 unicode
#author:Steven Huang 10/02/20
#function:common get html content by requests
import sys
import requests
import urllib.request
from .headersRandom import userAgentHeaders
from .userAgent import GetUA


def getUrlByUrllib(url):
    try:
        with urllib.request.urlopen(url) as response:
            charset = response.info().get_content_charset()
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
        return "Something Wrong!"
        

def getHtmlText(url):
    return getUrlByRequest(url)
    
def openUrl(url, save=False, file=r'./a.html'):
    html = getHtmlText(url)
    if save:
        saveToFile(html,file)
    return html

def saveToFile(html, file):
    with open(file, "w") as text_file:
        text_file.write(html)

def openUrlUrlLib(url):
    return getUrlByUrllib(url)   