# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from urllib.request import urlretrieve

class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0"}
    start_urls = ['http://douban.com/']

    def start_requests(self):
        return [Request('https://accounts.douban.com/login', callback=self.parse, meta={"cookiejar":1})]

    def parse(self, response):
        captcha = response.xpath("//img[@class='captcha_image']/@src").extract()

        # url = 'https://www.douban.com/accounts/login'
        url = 'https://accounts.douban.com/login'
        if len(captcha) > 0:
            print("有验证码的情况")
            localpath = "E:/171229model/0110captcha/douban.png"
            urlretrieve(captcha[0], filename=localpath)
            print("请查看本地验证码文件并输入")
            captcha_val = input()
            data = {
                "form_email": "xiaoliu920@163.com",
                "form_password": "hgj310620",
                "redir": "https://www.douban.com/people/27513368/",
                "captcha_solution": captcha_val,
            }

        else:
            data = {
                "form_email": "xiaoliu920@163.com",
                "form_password": "hgj310620",
                "redir": "https://www.douban.com/people/27513368/"
            }

        print("登录中...")
        return [FormRequest.from_response(response,
                                          meta={"cookiejar": response.meta['cookiejar']},
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.next,

                                          )]


    def next(self, response):
        print("登录成功...")
        title = response.xpath("/html/head/title").extract()
        print(title[0])