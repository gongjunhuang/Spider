# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from scrapy.http import Request

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cp01.54.00.00.00.00.html']



    def parse(self, response):
        item = DoubanItem()
        item['title'] = response.xpath("//a[@name='itemlist-title']/@title").extract()
        item['link'] = response.xpath("//a[@name='itemlist-title']/@href").extract()
        item['content'] = response.xpath("//p[@class='search_hot_word']/text()").extract()
        item['comment'] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        item['price'] = response.xpath("//span[@class='price_n']/text()").extract()[5:]
        item['press'] = response.xpath("//a[@name='itemlist-author']/text()").extract()
        yield item
        for i in range(2, 101):
            url = 'http://category.dangdang.com/pg'+str(i)+'-cp01.54.00.00.00.00.html'
            yield Request(url, callback=self.parse)


