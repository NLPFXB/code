#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
from dailianmeng.items import DailianmengItem
from scrapy.selector import Selector
from bs4 import BeautifulSoup

class mySpiders(scrapy.spider.Spider):
    name = 'spiderDailianmeng'
    start_urls = ['http://www.dailianmeng.com/p2pblacklist/index.html']
    pageNumbers = 0
    currentNum = 1

    def parse(self,response):
        self.currentNum+=1
        sel = Selector(response)
        self.pageNumbers = int(sel.xpath("//li[@class = 'last']/a/@href").extract()[0].split('=')[1])
        sel_items = sel.xpath('//tr[@class]')

        for sel_item in sel_items:
            item_string = sel_item.extract()
            bs_item_string = BeautifulSoup(item_string,"lxml")
            items_list = [ line.text for line in bs_item_string.find_all("td")]

            item = DailianmengItem()
            item['name'] = items_list[0]
            item['cardNum'] = items_list[1]
            item['mobliePhoneNumber'] = items_list[2]
            item['emailAddress'] = items_list[3]
            item['Principal'] = items_list[4]
            item['alreadyRepay'] = items_list[5]
            item['toRepay'] = items_list[6]
            item['loanTime'] = items_list[7]
            item['loanDays'] = items_list[8]

            yield item

        yield scrapy.Request('http://www.dailianmeng.com/p2pblacklist/index.html?P2pBlacklist_page='+str(self.currentNum)+'&ajax=yw0',method='get',callback=self.parse_item)

    def parse_item(self,response):
        if self.currentNum <= self.pageNumbers:
            self.currentNum+=1
            sel = Selector(response)
            sel_items = sel.xpath('//tr[@class]')

            for sel_item in sel_items:
                item_string = sel_item.extract()
                bs_item_string = BeautifulSoup(item_string,"lxml")
                items_list = [ line.text for line in bs_item_string.find_all("td")]

                item = DailianmengItem()
                item['name'] = items_list[0]
                item['cardNum'] = items_list[1]
                item['mobliePhoneNumber'] = items_list[2]
                item['emailAddress'] = items_list[3]
                item['Principal'] = items_list[4]
                item['alreadyRepay'] = items_list[5]
                item['toRepay'] = items_list[6]
                item['loanTime'] = items_list[7]
                item['loanDays'] = items_list[8]

                yield item

            yield scrapy.Request('http://www.dailianmeng.com/p2pblacklist/index.html?P2pBlacklist_page='+str(self.currentNum)+'&ajax=yw0',method='get',callback=self.parse_item)