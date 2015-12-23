__author__ = 'fengxiaobo'
#coding:utf-8
import scrapy
import requests
from scrapy.selector import Selector
from zhengxingSystem.items import ZhengxingsystemItem
import codecs
class SpiderZX(scrapy.spider.Spider):
    name = 'zhengxing'
    current = 3
    download_delay = 360
    # start_urls = ['http://www.11315.com/al/vl/' + str(1)]
    def start_requests(self):
        yield scrapy.Request("http://www.11315.com/al/vl/3",
                      headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"})
    def parse(self,response):
        data = 'userType=2&loginName=11315&password=pfrNYAosty&passt=6cc8f97c914a57702c206a81990d44e711990b7aff868677a05c9f84f9085f7d3b8c438706977aaa9184f6663003e5920f08b222c76139c7c7557d1de67eab36df9b4f3dd571dc36e0fefb2e3b3fdbf8357573be22ed31c8'
        res = requests.post(url = "http://www.11315.com/customer/ssologinvalid",data=data)
        if not self.isLastPage(response):
            self.current += 1
            nextUrl = 'http://www.11315.com/al/vl/' + str(self.current)
            for url in self.getNextUrls(response):
                url = 'http://www.11315.com'+ url
                yield scrapy.Request(url = url, callback= self.getItems, headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"})
            yield scrapy.Request(url = nextUrl,callback= self.parse, headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"})
    def getNextUrls(self,response):
        sel = Selector(response)
        urls = sel.xpath("//div[@class='tableWrap']/table[@class='listable']/tbody/tr/td[1]/a[@target]/@href").extract()
        return urls
    def getItems(self,response):
        sel = Selector(response)
        item = ZhengxingsystemItem()
        name1 = sel.xpath("//div[@class='f-cb pad10 ']/table[1]/tbody/tr[2]/td[2]/h1/b/a/text()").extract()
        registeredCapital1 = sel.xpath("//div[@class='f-cb pad10 ']/table[1]/tbody/tr[3]/td[4]/text()").extract()
        industry1 = sel.xpath("//div[@class='f-cb pad10 ']/table[1]/tbody/tr[4]/td[2]/text()").extract()
        region1 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tbody/tr[1]/td[2]/text()").extract()
        creditURL1 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tbody/tr[1]/td[4]/a/text()").extract()
        address1 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tbody/tr[2]/td[2]/text()").extract()
        businessWebsite1 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tbody/tr[2]/td[4]/a/text()").extract()
        mainProduct1 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tbody/tr[3]/td[2]/text()").extract()

        name2 = sel.xpath("//div[@class='f-cb pad10 ']/table[1]/tr[2]/td[2]/h1/b/a/text()").extract()
        registeredCapital2 = sel.xpath("//div[@class='f-cb pad10 ']/table[1]/tr[3]/td[4]/text()").extract()
        industry2 = sel.xpath("//div[@class='f-cb pad10 ']/table[1]/tr[4]/td[2]/text()").extract()
        region2 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tr[1]/td[2]/text()").extract()
        creditURL2 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tr[1]/td[4]/a/text()").extract()
        address2 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tr[2]/td[2]/text()").extract()
        businessWebsite2 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tr[2]/td[4]/a/text()").extract()
        mainProduct2 = sel.xpath("//div[@class='f-cb pad10 ']/table[2]/tr[3]/td[2]/text()").extract()
        item['name'] = '' if not name1 and not name2 else (name1 or name2)[0].strip()
        item['registeredCapital'] = '' if not registeredCapital1 and not registeredCapital2 else (registeredCapital1 or registeredCapital2)[0].strip()
        item['industry'] = '' if not industry1 and not industry2 else (industry1 or industry2)[0].strip()
        item['region'] = '' if not region1 and not region2 else (region1 or region2)[0].strip()
        item['creditURL'] = '' if not creditURL1 and not creditURL2 else (creditURL1 or creditURL2)[0].strip()
        item['address'] = '' if not address1 and not address2 else (address1 or address2)[0].strip()
        item['businessWebsite'] = '' if not businessWebsite1 and not businessWebsite2 else (businessWebsite1 or businessWebsite2)[0].strip()
        item['mainProduct'] = '' if not mainProduct1 and not mainProduct2 else (mainProduct1 or mainProduct2)[0].strip()
        yield item

    def isLastPage(self,response):
        sel = Selector(response)
        try:
            label = sel.xpath("//div[@class = 'paginator']/span[@class = 'prev']/text()").extract()[0]
        except:
            label = sel.xpath("//div[@class = 'paginator']/span[@class = 'prev']/text()").extract()
            if label == []:
                return False
        return label == '下一页'.decode('utf-8')
