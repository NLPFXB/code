# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhengxingsystemItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # legalRepresentative = scrapy.Field()
    registeredCapital = scrapy.Field()
    industry = scrapy.Field()
    region = scrapy.Field()
    creditURL = scrapy.Field()
    address = scrapy.Field()
    businessWebsite = scrapy.Field()
    mainProduct = scrapy.Field()
