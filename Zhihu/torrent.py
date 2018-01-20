
import requests
import re
from urllib.request import urlretrieve
import os
import time

headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
        "Referer": "http://javtorrent.re/"
    }
toHeader = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0'
}

proxy = {'http':'http://127.0.0.1:1080',
         'https': 'https://127.0.0.1:1080'}

#url = 'http://javtorrent.re/censored/143383/'
'''http://javtorrent.re/censored/114099/'''
path = 'E:/171229model/0114movie/'

def get_size(url):
    data = requests.get(url, headers=headers, proxies=proxy).text
    # print(data)
    titlePat = re.compile('<h1 class="entry-title">(.*?)</h1>')
    imgPat = re.compile('<img src="(//.*?.jpg)" class="s-full">')
    dlPat = re.compile('<a href="(//.*?)" class="dl-link DL" target="_blank">.*?GB</a><ul><li>')
    hdPat = re.compile('<a href="(//.*?hd)" class="dl-link HD" target="_blank">.*?GB</a><ul><li>')

    urlList = []
    dlList = []
    hdList = []
    dlList = re.findall(dlPat, data)
    if(len(dlList) == 0):
        hdList = re.findall(hdPat, data)
    urlList = dlList + hdList
    # 找到普通画质和hd画质的第一个链接作为下载链接
    next = 'http:' + urlList[0]

    nextUrl, torrentUrl = get_torrent(next)
    print(torrentUrl)
    # 找到torrent文件名
    index = torrentUrl.rindex('/')
    torrentName = torrentUrl[index:]
    print(torrentName)

    # 获取封面图片下载路径
    imgUrl = re.findall(imgPat, data)[0]
    imgUrl = 'http:' + imgUrl

    # 获取片名
    title = re.findall(titlePat, data)[0]
    # 本地下载路径
    filepath = path + str(title)

    if not os.path.exists(filepath):
        os.mkdir(filepath)
    imgPath = filepath + '/cover.jpg'
    toPath = filepath + torrentName
    # 下载
    download_img(imgUrl, imgPath)
    download_torrent(torrentUrl, toPath, nextUrl)

# 返回种子文件的下一个链接和种子下载链接，并把nextUrl作为下载种子文件的referer
def get_torrent(url):
    data = requests.get(url, headers=headers, proxies=proxy).text
    nextLink = re.compile('<a href="(http:.*?)" class="j-link">Click to Link</a>')
    nextUrl = re.findall(nextLink, data)
    nextUrl = nextUrl[0]
    torrentdata = requests.get(nextUrl, headers=headers, proxies=proxy).text
    torrentPat = re.compile('<a href="(http://.*?.torrent)" class="j-link">Download')
    torrentUrl = re.findall(torrentPat, torrentdata)
    torrentUrl = torrentUrl[0]
    return nextUrl, torrentUrl

# 下载图片文件，对referer要求不高
def download_img(url, filename):
    res = requests.get(url, headers=headers, proxies=proxy)

    with open(filename, 'wb') as f:
        f.write(res.content)

# 下载torrent文件，要求referer为上一级链接
def download_torrent(url, filename, referer):
    session = requests.session()
    session.headers.update({'referer': referer})
    res = session.get(url, headers=toHeader, proxies=proxy)

    with open(filename, 'wb') as f:
        f.write(res.content)

if __name__ == '__main__':
    for i in range(114099, 120000):
        url = 'http://javtorrent.re/censored/' + str(i)
        try:
            get_size(url)
            time.sleep(0.1)
        except Exception as e:
            print(e)