# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://dangdang.com/']

    def start_requests(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 \
                      Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent': user_agent}
        yield scrapy.Request(url=self.start_urls, headers=headers, method='GET', callback=self.parse)

    def parse(self, response):
        item = DoubanItem()
        item['title'] = response.xpath("//a[@name='itemlist-title']/@title").extract()
        item['link'] = response.xpath("//a[@name='itemlist-title']/@href").extract()
        item['content'] = response.xpath("//p[@class='search_hot_word']/text()").extract()
        item['comment'] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        item['price'] = response.xpath("//span[@class='price_n']/text()").extract()
        yield item


