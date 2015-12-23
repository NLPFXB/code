# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Mo9Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    accountName = scrapy.Field() #账户名称
    name = scrapy.Field()
    cardNum = scrapy.Field()
    arrears = scrapy.Field() #欠款金额
    overdueDays = scrapy.Field()#逾期天数
