# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhixingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    caseCode = scrapy.Field()
    caseState = scrapy.Field()
    execCourtName = scrapy.Field()
    execMoney = scrapy.Field()
    partyCardNum = scrapy.Field()
    pname = scrapy.Field()
    caseCreateTime = scrapy.Field()