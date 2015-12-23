# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KaikaidaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    cardNum = scrapy.Field()
    address = scrapy.Field()
    company = scrapy.Field()#公司名称
    company_address = scrapy.Field()#公司地址
    email_address = scrapy.Field()
    telePhoneNumbers = scrapy.Field()
    mobilePhoneNumber = scrapy.Field()
    overdueRepaymentNum = scrapy.Field()#几笔逾期未还款
    websitePayNum = scrapy.Field()#几笔网站垫付款
    overdueDays = scrapy.Field()#最长逾期天数
    overdueRepaymentTotal = scrapy.Field()#逾期待还总额
