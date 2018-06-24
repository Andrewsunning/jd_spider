# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class JdSpiderPipeline(object):
    def process_item(self, item, spider):
        f = open(r'./123.csv', 'a+')
        writer = csv.writer(f)
        writer.writerow((item['ID'],item['name'], item['link'],item['comment_num'], item['shop_name'], item['price'], item['good_count'], item['general_count'], item['poor_count']))

        return item
