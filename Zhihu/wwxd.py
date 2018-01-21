import requests
import pandas as pd
import re
import time
import random
import string

url = 'https://movie.douban.com/subject/6874741/comments?start=20&amp;limit=20&amp;sort=new_score&amp;status=P&amp;percent_type='
url_begin = 'https://movie.douban.com/subject/6874741/comments'

data = {
                    "form_email": "xiaoliu920@163.com",
                    "form_password": "hgj310620",
                    "redir": "https://movie.douban.com/subject/6874741/comments"
                }

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Host": "movie.douban.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN, zh; q=0.8, en; q=0.6",
        "Referer": "https://movie.douban.com/subject/6874741/comments?status=P",

    }

#cookies = {'cookie': "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))}
cookies = {'cookies': 'bid=K9l10zjVUkk'}

'''votes    有用    点评人    看过    score'''
nextPat = re.compile(r'<a href="(.*?)".*?class="next">后页')
commentPat = re.compile(r'<p class="">(.*?)')
re_content = re.compile(r'<span class="votes">(.*?)</span>.*?comment">(.*?)</a>.*?</span>.*?<span.*?class="">(.*?)</a>.*?<span>(.*?)</span>.*?title="(.*?)"></span>.*?title="(.*?)">.*?class=""> (.*?)\n', re.S)
contentPat = re.compile(r'<span class="votes">(.*?)</span>.*?<a href=.*?>(.*?)</a>.*?<a href=.*?class="">(.*?)</a>.*?<span>(.*?)</span>.*?<span.*?rating" title="(.*?)"></span>.*?<span.*?title="(.*?)">.*?</span>.*?<p class="">(.*?)\n', re.S)
session = requests.session()
html = session.post(url, headers=headers, cookies=cookies)
header = ['Votes', 'Useful', 'Commentor', 'Watched', 'Score', 'Comments']
while html.status_code == 200:
    nextLink = re.findall(nextPat, html.text)
    if len(nextLink) > 0:
        nextLink = nextLink[0]
    else:
        break
    nextLink = nextLink.replace('&amp;', '&')
    next_page = url_begin + nextLink
    print(next_page)
    content = re.findall(contentPat, html.text)
    #print(content)
    frame = pd.DataFrame(content)
    frame.to_csv('E:\BaiduNetdiskDownload\第14章 文本挖掘\wwxd.csv', header=False, index=False, mode='a+')
    time.sleep(1)
    content = []
    frame = []
    html = requests.get(next_page, headers=headers, cookies=cookies)




