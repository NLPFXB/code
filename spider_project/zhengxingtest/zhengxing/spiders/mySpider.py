#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
from scrapy.selector import Selector

class mySPider(scrapy.spider.Spider):
    name = 'testSpider'
    url = 'http://www.11315.com/al/vl/'
    begin = 1
    download_delay = 10
    #start_urls = [url+str(begin)]
    def start_requests(self):
        yield scrapy.Request(self.url+str(self.begin),
                      headers={'User-Agent': "User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},dont_filter=True)
    def parse(self,response):
        if not self.isLastPage(response):
            with open(str(self.begin)+'.txt','w') as f:
                f.write(response.body)
            self.begin += 1
            print response.url,"=============================="
            yield scrapy.Request(self.url + str(self.begin),
                      headers={'User-Agent': "User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},dont_filter=True)
    def isLastPage(self,response):
        sel = Selector(response)
        try:
            label = sel.xpath("//div[@class = 'paginator']/span[@class = 'prev']/text()").extract()[0]
        except:
            label = sel.xpath("//div[@class = 'paginator']/span[@class = 'prev']/text()").extract()
            if label == []:
                return False
        return label == '下一页'.decode('utf-8')
