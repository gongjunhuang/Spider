
import requests
import re
from urllib.request import urlretrieve

headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0'
    }

proxy = {'http':'http://127.0.0.1:1080',
         'https': 'https://127.0.0.1:1080'}

url = 'http://javtorrent.re/censored/143163/'

def get_size():
    data = requests.get(url, headers=headers, proxies=proxy).text
    # print(data)
    titlePat = re.compile('<h1 class="entry-title">(.*?)</h1>')
    imgPat = re.compile('<img src="(//jtl.re/x/18/ssni101.jpg)" class="s-full">')
    dlPat = re.compile('<a href="(//.*?)" class="dl-link DL" target="_blank">.*?GB</a><ul><li>')
    hdPat = re.compile('<a href="(//.*?)" class="dl-link HD" target="_blank">.*?GB</a><ul><li>')

    urlList = []
    dlList = re.findall(dlPat, data)
    hdList = re.findall(hdPat, data)
    urlList = dlList + hdList
    print(hdList)
if __name__ == '__main__':
    get_size()
