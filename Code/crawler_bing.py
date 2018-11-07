#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request

import requests
#import urllib
from bs4 import BeautifulSoup
import os

if os.path.exists('image') == True:  # 如果目录不存在则创建
    print("image dir is exsit")
else:
    os.mkdir('image')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/35.0.1916.114 Safari/537.36',
    'Cookie': 'AspxAutoDetectCookieSupport=1'
}

i = 0
#for page in range(1,2):
url = 'https://bing.ioliu.cn/?p=1'# + str(page)
r = requests.get(url)
contents = r.text

soup = BeautifulSoup(contents, 'html.parser')
divs = soup.find_all('div', 'item')

for div in divs:
    imgs = div.find_all('img')
    for img in imgs:
        #print(img['src'])
        print(img['src'].replace('400x240', '1920x1080'))

        request = urllib.request.Request(img['src'].replace('400x240', '1920x1080'), None, header)
        response = urllib.request.urlopen(request)
        #with open('D:/Work/PythonCode/Crawler/image/'+img['src'].replace('400x240', '1920x1080'), "wb") as f:
        with open('image/%s.jpg' % i, "wb") as f:
            f.write(response.read())
        i += 1
        print('成功抓取第%s张图片' % i)
print('共抓取'+str(i)+'张图片')
#打exe专用指令pyinstaller -F "D:\Work\PythonCode\Crawler\crawler_bing.py"