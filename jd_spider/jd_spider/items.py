# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item

class goodsItem(Item):
    link = Field()  # 商品链接 1
    ID = Field()  # 商品ID 2
    name = Field()  # 商品名字 3
    comment_num = Field()  # 评论人数 6
    shop_name = Field()  # 店家名字 4
    price = Field()  # 价钱 5
    # commentVersion = Field()  # 为了得到评论的地址需要该字段
    good_count = Field()  # 好评人数
    general_count = Field()  # 中评人数
    poor_count = Field()  # 差评人数