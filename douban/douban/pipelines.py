# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def process_item(self, item, spider):
        for i in range(0, len(item['title'])):
            title = item['title'][i]
            link = item['link'][i]
            content = item['content'][i]
            comment = item['comment'][i]
            price = item['price'][i]
        return item
