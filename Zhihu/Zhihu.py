
import requests
import os
import json
from bs4 import BeautifulSoup
import time
import re

def login():
    url = 'http://www.zhihu.com'
    loginURL = 'http://www.zhihu.com/login/email'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
        "Referer": "http://www.zhihu.com/",
        'Host': 'www.zhihu.com',
    }

    data = {
        'email': 'xiaoliu920@163.com',
        'password': 'zhihu_310620',
        'rememberme': 'true'
    }

    global s
    s = requests.session()
    global xsrf
    if os.path.exists("cookiefile"):
        with open('cookiefile') as f:
            cookie = json.load(f)
        s.cookies.update(cookie)
        req1 = requests.get(url, headers=headers)
        soup = BeautifulSoup(req1.text, 'html.parser')
        xsrf = re.findall('xsrf.*?;:.*?;([A-Za-z0-9\-]*)&quot', req1.text)[0]
        # 建立一个zhihu.html，用于验证是否登录成功
        req1.encoding = 'utf-8'
        with open('zhihu.html', 'wb') as f:
            f.write(req1.content)
    else:
        req = s.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        #xsrf = re.findall('name="_xsrf" value="([\S\s]*?)"', req.text)[0]
        xsrf = re.findall('xsrf.*?;:.*?;([A-Za-z0-9\-]*)&quot', req.text)[0]
        data['_xsrf'] = xsrf
        timestamp = int(time.time() * 1000)
        captchaUrl = 'http://www.zhihu.com/captcha.gif?=' + str(timestamp)
        print(captchaUrl)

        with open('E:/171229model/0114zhihu/zhihuCaptcha.gif', 'wb') as f:
            captReq = s.get(captchaUrl, headers=headers)
            f.write(captReq.content)

        loginCapt = input('please input your captcha:').strip()
        data['captcha'] = loginCapt
        print(data)
        loginReq = s.post(loginURL, headers=headers, data=data, verify=True)
        #data = loginReq.json()
        status = re.findall('.*?(200).*?', str(loginReq))
        if status:
            print(s.cookies.get_dict())
            with open('cookiefile', 'w') as f:
                json.dump(s.cookies.get_dict(), f)
        else:
            print('login failed')



if __name__ == '__main__':
    login()