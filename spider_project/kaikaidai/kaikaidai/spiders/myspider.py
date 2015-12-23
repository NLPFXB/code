#coding:gbk
__author__ = 'fengxiaobo'
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
from kaikaidai.items import KaikaidaiItem

class KaikaidaiSpider(scrapy.spider.Spider):
    name = 'kaikaidaiSpider'
    start_urls = ['http://www.kaikaidai.com/Lend/Black.aspx']
    totalPageNumbers = 0
    currentPageNumber = 1
    DOWNLOAD_DELAY = 1
    params = {'__EVENTTARGET':'rpMessage',
              '__EVENTARGUMENT':'pager$'}

    def parse(self,response):
        self.totalPageNumbers = self.get_total_page_numbers(response)

        sel = Selector(response)
        items_selectors = sel.xpath("//table[@class='hmd_ytab']")
        for items in items_selectors:
            item = KaikaidaiItem()
            bs4_items = BeautifulSoup(items.extract(),"lxml")
            items_list = [line.strip() for line in bs4_items.text.split('\n') if line.strip()]
            # print '==================='
            # print len(items_list)
            # print '\n'.join(items_list)
            item['name'] = items_list[1]
            item['cardNum'] = items_list[8]
            item['address'] = items_list[15]
            item['company'] = items_list[22]
            item['company_address'] = items_list[-1]
            item['email_address'] = items_list[3]
            item['telePhoneNumbers'] = items_list[10]
            item['mobilePhoneNumber'] = items_list[17]
            item['overdueRepaymentNum'] = items_list[5]
            item['websitePayNum'] = items_list[12]
            item['overdueDays'] = items_list[19]
            item['overdueRepaymentTotal'] = items_list[24][1:]

            yield item
        self.params['__EVENTARGUMENT'] = 'pager$'+str(self.currentPageNumber)
        yield scrapy.FormRequest('http://www.kaikaidai.com/Lend/Black.aspx',method='post',formdata=self.params,callback=self.parse_after_page)
    def parse_after_page(self,response):
        if self.currentPageNumber < self.totalPageNumbers:
            self.currentPageNumber += 1
            sel = Selector(response)
            items_selectors = sel.xpath("//table[@class='hmd_ytab']")

            for items in items_selectors:
                item = KaikaidaiItem()
                bs4_items = BeautifulSoup(items.extract(),"lxml")
                items_list = [line.strip() for line in bs4_items.text.split('\n') if line.strip()]
                if 'E_mail' not in items_list[2]:
                    del items_list[2]
                item['name'] = items_list[1]
                item['cardNum'] = items_list[8]
                item['address'] = items_list[15]
                item['company'] = items_list[22]
                item['company_address'] = items_list[-1]
                item['email_address'] = items_list[3]
                item['telePhoneNumbers'] = items_list[10]
                item['mobilePhoneNumber'] = items_list[17]
                item['overdueRepaymentNum'] = items_list[5]
                item['websitePayNum'] = items_list[12]
                item['overdueDays'] = items_list[19]
                item['overdueRepaymentTotal'] = items_list[24][1:]

                yield item
            self.params['__EVENTARGUMENT'] = 'pager$'+str(self.currentPageNumber)
            yield scrapy.FormRequest('http://www.kaikaidai.com/Lend/Black.aspx',method='post',formdata = self.params,callback=self.parse_after_page)

    def get_total_page_numbers(self,response):
        sel = Selector(response)
        response_page_list = sel.xpath("//div[@class='pager']/table/tr/td/text()").extract()
        response_page = response_page_list[0].strip().split('/')[1][1:-1]
        return int(response_page)