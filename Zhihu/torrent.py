
import requests
import re
from urllib.request import urlretrieve
import os

headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0'
    }

proxy = {'http':'http://127.0.0.1:1080',
         'https': 'https://127.0.0.1:1080'}

url = 'http://javtorrent.re/censored/143383/'
path = 'E:/171229model/0114movie/'

def get_size():
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
    next = 'http:' + urlList[0]
    torrentUrl = get_torrent(next)
    print(torrentUrl)
    imgUrl = re.findall(imgPat, data)[0]
    imgUrl = 'http:' + imgUrl

    title = re.findall(titlePat, data)[0]
    print(imgUrl)
    print(title)
    filepath = path + str(title)
    print(filepath)

    if not os.path.exists(filepath):
        os.mkdir(filepath)
        imgPath = filepath + '/1.jpg'
        toPath = filepath + '/1.torrent'
        #urlretrieve('1.jpg', filepath)
        #urlretrieve(torrentUrl, filepath)
        download(imgUrl, imgPath)
        download(torrentUrl, toPath)

def get_torrent(url):
    data = requests.get(url, headers=headers, proxies=proxy).text
    nextLink = re.compile('<a href="(http:.*?)" class="j-link">Click to Link</a>')
    nextUrl = re.findall(nextLink, data)
    nextUrl = nextUrl[0]
    torrentdata = requests.get(nextUrl, headers=headers, proxies=proxy).text
    torrentPat = re.compile('<a href="(http://.*?.torrent)" class="j-link">Download')
    torrentUrl = re.findall(torrentPat, torrentdata)
    torrentUrl = torrentUrl[0]
    return torrentUrl

def download(url, filename):
    res = requests.get(url, headers=headers, proxies=proxy)
    with open(filename, 'wb') as f:
        f.write(res.content)

if __name__ == '__main__':
    get_size()
