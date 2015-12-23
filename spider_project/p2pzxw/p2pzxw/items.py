# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class P2PzxwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() #姓名
    cardNum = scrapy.Field() #证件号
    sex = scrapy.Field() #性别
    cardAddress = scrapy.Field() #身份证地址
    homeAddress = scrapy.Field() #家庭地址
    contactNumber = scrapy.Field() #联系电话
    ArrearsTotal = scrapy.Field() #欠款本息总额
    TotalPenalty = scrapy.Field() #逾期总罚金
    OverdueNum = scrapy.Field() #逾期笔数
    websiteNum = scrapy.Field() #网站代还笔数
    OverdueDays = scrapy.Field() #最长逾期天数
    updateTime = scrapy.Field() #更新时间


