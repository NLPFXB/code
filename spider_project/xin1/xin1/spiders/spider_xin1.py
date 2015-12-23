#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
from xin1.items import Xin1Item
from scrapy.selector import Selector
from bs4 import BeautifulSoup
import urllib

class mySpider(scrapy.spider.Spider):
    name = 'xin1Spider'
    start_urls = ['http://www.xin1.com/Black/BlackPub.aspx']
    totalPageNumbers = 0
    currentPageNumber = 1
    DOWNLOAD_DELAY = 1
    params = {'__EVENTTARGET':'rpMessage',
              '__EVENTARGUMENT':'pager$'}

    def parse(self,response):
        self.totalPageNumbers = self.get_total_page_numbers(response)

        sel = Selector(response)
        items_selectors = sel.xpath("//dl[@class='bla_dlk']")
        for items in items_selectors:
            item = Xin1Item()
            bs4_items = BeautifulSoup(items.extract())
            items_list = [p.text for p in bs4_items.find_all('span')]
            item['name'] = items_list[0]
            item['cardNum'] = items_list[1]
            item['address'] = items_list[2]
            item['lender'] = items_list[3]
            item['lendMoney'] = items_list[4][1:]

            yield item
        self.params['__EVENTARGUMENT'] = 'pager$'+str(self.currentPageNumber)
        yield scrapy.FormRequest('http://www.xin1.com/Black/BlackPub.aspx',method='post',formdata=self.params,callback=self.parse_after_page)
    def parse_after_page(self,response):
        if self.currentPageNumber < self.totalPageNumbers:
            self.currentPageNumber += 1
            sel = Selector(response)
            items_selectors = sel.xpath("//dl[@class='bla_dlk']")
            for items in items_selectors:
                item = Xin1Item()
                bs4_items = BeautifulSoup(items.extract())
                items_list = [p.text for p in bs4_items.find_all('span')]
                item['name'] = items_list[0]
                item['cardNum'] = items_list[1]
                item['address'] = items_list[2]
                item['lender'] = items_list[3]
                item['lendMoney'] = items_list[4][1:]

                yield item
            self.params['__EVENTARGUMENT'] = 'pager$'+str(self.currentPageNumber)
            yield scrapy.FormRequest('http://www.xin1.com/Black/BlackPub.aspx',method='post',formdata   =self.params,callback=self.parse_after_page)

    def get_total_page_numbers(self,response):
        sel = Selector(response)
        response_page_list = sel.xpath("//div[@class='pager']/table/tr/td/text()").extract()
        response_page = response_page_list[0][2:-2].split('/')[1][1:-1]
        return int(response_page)