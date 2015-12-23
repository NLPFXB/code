# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item
class PpaiItem(Item):
    user_name = Field() #用户名
    peron_name = Field() #姓名
    mobilephone_number = Field() #手机号
    identitycard= Field() #身份证号
    borrow_period = Field() #借款期数
    borrow_time = Field() #借款时间
    overduecharge = Field() #逾期本息
    own_Money = Field() #本金
    over_days = Field() #逾期天数
