# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from jd_spider.items import goodsItem
from scrapy.selector import Selector
import scrapy
import json

class JdSpider(scrapy.Spider):
    name = "jd"
    # allowed_domains = ["jd.com"]
    start_urls = ['http://search.jd.com/Search?keyword=%E8%BF%9B%E5%8F%A3%E7%89%9B%E5%A5%B6&enc=utf-8&pvid=834d3964580f489ab4f86aa8a54f207a']


    def parse_getCommentnum(self, response):
        item1 = response.meta['item']
        # response.body是一个json格式的
        # print(response.body)
        # print(type(response.body))
        # print(str(response.body))
        # print(type(response.body))
        js = json.loads(response.body.decode('gbk', 'ignore'))
        print(type(js))
        item1['good_count'] = js['CommentsCount'][0]['GoodCount']
        item1['general_count'] = js['CommentsCount'][0]['GeneralCount']
        item1['poor_count'] = js['CommentsCount'][0]['PoorCount']
        item1['comment_num'] = js['CommentsCount'][0]['CommentCount']
        print(item1['good_count'], item1['general_count'], item1['poor_count'], item1['comment_num'])
        return item1

    def parse_detail(self, response):
        item1 = response.meta['item']
        sel = Selector(response)

        url = "http://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + str(item1['ID'])
        print(url)
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_getCommentnum)

    def parse(self, response):  # 解析搜索页
        sel = Selector(response)  # Xpath选择器
        goods = sel.xpath('//li[@class="gl-item"]')
        for good in goods:
            item1 = goodsItem()
            item1['ID'] = good.xpath('./@data-sku').extract()[0]
            item1['name'] = good.xpath('./div/div[@class="p-name p-name-type-2"]/a/em/text()').extract()[0]
            # print(type(good.xpath('./div/div[@class="p-name p-name-type-2"]/a/em/text()').extract()))
            if good.xpath('./div/div[contains(@class,"p-shop")]/span/a/text()').extract():
                item1['shop_name'] = good.xpath('./div/div[contains(@class,"p-shop")]/span/a/text()').extract()[0]
            else:
                item1['shop_name'] = ''
            item1['link'] = good.xpath('./div/div[@class="p-img"]/a/@href').extract()[0]
            item1['price'] = good.xpath('./div//div[@class="p-price"]/strong/i/text()').extract()[0]

            item1['comment_num'] = good.xpath('./div//div[@class="p-commit"]/strong/a/text()').extract()[0]
            print(item1['ID'], item1['name'], item1['shop_name'], item1['price'])
            if item1['link'].startswith('http'):
                url = item1['link']
            else:
                url = "http:" + item1['link']
            yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_detail)