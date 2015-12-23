# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KuaichainfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name  = scrapy.Field()#姓名
    area = scrapy.Field() #户口所在地
    cardNum = scrapy.Field() #身份证
    case = scrapy.Field() #违规案件的具体信息
