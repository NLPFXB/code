#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
from mo9.items import Mo9Item
import re
import math
from scrapy.selector import Selector
from bs4 import BeautifulSoup
class SpiderMo09(scrapy.spider.Spider):

    name = 'mo09spider'
    start_urls = ['https://www.mo9.com/creditCenter/']
    # download_delay = 10
    totalPageNumber = 0
    currentPageNumber = 1398
    page_2_url  = 'https://www.mo9.com/creditCenter/p/2'
    page_url = 'https://www.mo9.com/creditCenter/p/'

    def parse(self,response):
        pageNumberList = self.getTotalPageNumber(response.body)
        self.totalPageNumber = int(math.ceil(pageNumberList[0]/pageNumberList[1]))

        sel = Selector(response)
        items = sel.xpath("//dl[@class='bg-gray fs12 clearfix clear']|//dl[@class='bg-white fs12 clearfix clear']")
        person_info_list = [BeautifulSoup(item.extract(),"lxml") for item in items]
        for person in person_info_list:
            person_info = person.text.strip().split()

            item = Mo9Item()
            item['accountName'] = person_info[0]
            item['name'] = person_info[1]
            item['cardNum'] = person_info[2]
            item['arrears'] = person_info[3]
            item['overdueDays'] = person_info[4]

            yield item
        self.currentPageNumber += 1
        yield scrapy.Request(self.page_2_url,callback = self.after_parse)
    def after_parse(self,response):
        if self.currentPageNumber < self.totalPageNumber:
            self.currentPageNumber += 1
            sel = Selector(response)
            items = sel.xpath("//dl[@class='bg-gray fs12 clearfix clear']|//dl[@class='bg-white fs12 clearfix clear']")
            person_info_list = [BeautifulSoup(item.extract(),"lxml") for item in items]
            for person in person_info_list:
                person_info = person.text.strip().split()

                item = Mo9Item()
                item['accountName'] = person_info[0]
                item['name'] = person_info[1]
                item['cardNum'] = person_info[2]
                item['arrears'] = person_info[3]
                item['overdueDays'] = person_info[4]

                yield item
            yield scrapy.Request(self.page_url + str(self.currentPageNumber), callback=self.after_parse)

    def getTotalPageNumber(self,body):
        pattern = re.compile(r"items(.*\d+)\"")
        reResult = pattern.findall(body)
        numberPattern = re.compile(r"\d+")
        res = [ float(numberPattern.search(line).group()) for line in reResult]
        return res

