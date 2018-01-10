# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TsPipeline(object):

    def __init__(self):
        self.fh = open('E:/171229model/tianshan/lesson.txt', 'w')

    def process_item(self, item, spider):
        print(item['title'])
        print(item['link'])
        print(item['student'])
        print('----------------')
        self.fh.write(item['title'][0]+'\n'+item['link'][0]+'\n'+item['student'][0]+'\n'+'----------------\n')
        return item

    def close_spider(self):
        self.fh.close()
