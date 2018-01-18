import requests
import re
import datetime
import os
from urllib.request import urlretrieve

headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0'
    }

proxy = {'http':'http://127.0.0.1:1080',
         'https': 'https://127.0.0.1:1080'}

url = 'http://t66y.com/htm_data/7/1801/2423174.html'

data = requests.get(url, headers=headers, proxies=proxy).text
imgPat = re.compile("src='(http://.*?jpg)' onclick")
imgList = re.findall(imgPat, data)
for i in range(len(imgList)):
    img = imgList[i]
    filepath = 'E:/171229model/0114movie/' + str(i) + '.jpg'
    urlretrieve(img, filepath)
    print('正在下载第%d张图片'%i)


