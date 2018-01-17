import requests
import re
import datetime
import os
import random
from urllib.request import urlretrieve
import pymysql
import shutil

headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0'
    }

proxy = {'http':'http://127.0.0.1:1080',
         'https': 'https://127.0.0.1:1080'}

url = 'https://www.pornhub.com/view_video.php?viewkey=ph59fad27825a5a'

def download_the_movie(url):
    filepath = 'E:/171229model/0114movie/'
    req = requests.get(url, headers=headers, proxies=proxy).text
    if len(req) < 100:
        print('maybe errors about your urls')
        return
    titlePat = re.compile('<title>(.*?)</title>')
    movieUrlPat = re.compile('"videoUrl":"(https.*?)"},')
    titleOri = re.findall(titlePat, req)
    title = titleOri[0].split('-')[0].strip()
    # title = filter(lambda x: x in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _-", title)
    print(title)
    movieUrls = re.findall(movieUrlPat, req)
    time = datetime.datetime.now()
    time = str(time)[:10]
    # 720p格式
    hqUrl = movieUrls[0].replace('\\', '')
    print(hqUrl)
    downloadpath = filepath + time + str(2) + '.mp4'
    save_file(hqUrl, downloadpath)

def save_file(url, filepath):
    print('====下载中====')
    time1 = datetime.datetime.now()
    if os.path.isfile(filepath):
        file_size = os.path.getsize(filepath) / 1024 / 1024
        print('file' + filepath + 'already exists')
        return
    else:
        print('downloading '+ filepath + '...')
        req = requests.get(url, headers=headers, proxies=proxy, stream=True)
        print(req.content)
        #urlretrieve(url, filepath)
        with open(filepath, 'wb') as f:

            shutil.copyfileobj(req.raw, f)
        time2 = datetime.datetime.now()
        print(str(time2)[:-7])
        print(filepath + 'done')
        usedtime = time2 - time1
        file_size = os.path.getsize(filepath) / 1024 / 1024
        print('time used '+ str(usedtime)[:-7])
        print('file size is '+ file_size + ' and speed is '+ str(file_size / usedtime))
        return

if __name__ == '__main__':
    download_the_movie(url)