# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from urllib.request import urlopen

from douban.items import DoubanItem


class JdSpider(CrawlSpider):
    name = 'JD'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        try:
            item = DoubanItem()
            thisurl = response.url
            pattern = "item.jd.com/(.*?).html"
            x = re.search(pattern, thisurl)
            if(x):
                thisId = re.compile(pattern).findall(thisurl)[0]
                print(thisId)
                title = response.xpath("//html/head/title/text()").extract()
                shop = response.xpath("div[@class='name']/a[@target='_blank']/text()").extract()
                shop_link = response.xpath("div[@class='name']/a[@target='_blank']/@href").extract()
                priceurl = 'https://p.3.cn/prices/mgets?callback=jQuery1946753&type=1&area=1&pdtk=&pduid=1072980774&pdpin=&pin=null&pdbp=0&skuIds=J_'+str(thisId)+'&ext=11000000&source=item-pc'
                commenturl = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv5039&productId='+ str(thisId)+'&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1'

                priceData = urlopen(priceurl).read().decode('utf-8', 'ignore')
                commentData = urlopen(commenturl).read().decode('utf-8', 'ignore')
                pricePat = '"p":"(.*?)"'
                commentPat = '"goodRateShow":(.*?),'
                price = re.compile(pricePat).findall(priceData)
                comment = re.compile(commentPat).findall(commentData)

                if (len(title) and len(shop) and len(shop_link) and len(price) and len(comment)):
                    print(title[0])
                    print(shop[0])
                    print(shop_link[0])
                    print(price[0])
                    print(comment[0])
                    print('=========')
                else:
                    pass
            else:
                pass
        except Exception as e:
            print(e)
