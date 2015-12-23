# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DailianmengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    cardNum = scrapy.Field()
    mobliePhoneNumber = scrapy.Field()
    emailAddress = scrapy.Field()
    Principal = scrapy.Field() #本金
    alreadyRepay = scrapy.Field()
    toRepay = scrapy.Field()
    loanTime = scrapy.Field() #借款时间
    loanDays = scrapy.Field()
