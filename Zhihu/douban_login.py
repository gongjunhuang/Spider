# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import pandas as pd
import time
from http import cookiejar
import random
import string


url = 'https://accounts.douban.com/login'
url_begin = 'https://movie.douban.com/subject/6874741/comments'
#构造post数据
data={
    'redir': 'https://movie.douban.com/subject/6874741/comments?start=20&limit=20&sort=new_score&status=P&percent_type=',
    "form_email": "xiaoliu920@163.com",
    "form_password": "hgj310620",
    'login':u'登录'
}

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

session = requests.session()

session.cookies = cookiejar.LWPCookieJar(filename='cookies')
try:
    print(session.cookies)
    session.cookies.load(ignore_discard=True)
except Exception as e:
    print(e)
html = session.post(url, data, headers=headers)
page = html.text
#print(page)
#利用bs4获得验证码图片地址
soup = BeautifulSoup(page, "html.parser")
captcha_url = soup.find('img', id='captcha_image')
if captcha_url is not None:
    captcha_url = captcha_url['src']
    #利用正则获得验证码ID
    pattern = re.compile('<input type="hidden" name="captcha-id" value="(.*?)"/')
    captcha_id = re.findall(pattern, page)
    #将验证码图片保存到本地
    urlretrieve(captcha_url, "E:\BaiduNetdiskDownload\第14章 文本挖掘\captcha.jpg")
    captcha = input('please input the captcha:')
    data['captcha-solution'] = captcha
    data['captcha-id'] = captcha_id
html = session.post(url, data=data, headers=headers)
print(html.text)
session.cookies.save()

'''votes    有用    点评人    看过    score'''
nextPat = re.compile(r'<a href="(.*?)".*?class="next">后页')
commentPat = re.compile(r'<p class="">(.*?)')
re_content = re.compile(r'<span class="votes">(.*?)</span>.*?comment">(.*?)</a>.*?</span>.*?<span.*?class="">(.*?)</a>.*?<span>(.*?)</span>.*?title="(.*?)"></span>.*?title="(.*?)">.*?class=""> (.*?)\n', re.S)
contentPat = re.compile(r'<span class="votes">(.*?)</span>.*?<a href=.*?>(.*?)</a>.*?<a href=.*?class="">(.*?)</a>.*?<span>(.*?)</span>.*?<span.*?rating" title="(.*?)"></span>.*?<span.*?title="(.*?)">.*?</span>.*?<p class="">(.*?)\n', re.S)
#cookies = {'cookies': 'bid=K9l10zjVUkk'}
cookies = {'cookie': "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))}

'''https://movie.douban.com/subject/6874741/comments?start=220&limit=20&sort=new_score&status=P&percent_type='''


'''
while html.status_code == 200:
    nextLink = re.findall(nextPat, html.text)[0]

    nextLink = nextLink.replace('&amp;', '&')
    next_page = url_begin + nextLink
    print(next_page)
'''
for i in range(20, 10000, 20):
    nextLink = 'https://movie.douban.com/subject/6874741/comments?start=' + str(i) + '&limit=20&sort=new_score&status=P&percent_type='
    content = re.findall(contentPat, html.text)
    print(nextLink)
    frame = pd.DataFrame(content)
    frame.to_csv('E:\BaiduNetdiskDownload\第14章 文本挖掘\wwxd.csv', header=False, index=False, mode='a+')
    time.sleep(1)
    content = []
    frame = []
    #html = requests.get(next_page, headers=headers, cookies=cookies)
    html = session.post(nextLink, headers=headers)
    print(html.status_code)
