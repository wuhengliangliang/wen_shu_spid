# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WenShuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class Wen_Shu_ArticleItem(scrapy.Item):#创建字段存入数据库中
    title = scrapy.Field()
    datetime1 = scrapy.Field()
    content = scrapy.Field()