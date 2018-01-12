# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def process_item(self, item, spider):
        for i in range(len(item['title'])):
            print(item['title'][i])
            print(item['link'][i])
            print(item['content'][i])
            print(item['comment'][i])
            print(item['price'][i])
            print(item['press'][i])
            print('===============')

        return item
