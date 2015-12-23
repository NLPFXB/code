# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobuiItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    citySpell = scrapy.Field()
    dateTime = scrapy.Field()
    sampleSize = scrapy.Field()
    salary = scrapy.Field()