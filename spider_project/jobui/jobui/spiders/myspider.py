__author__ = 'fengxiaobo'
#coding:utf-8
import scrapy
from jobui.items import JobuiItem
from scrapy.selector import Selector

class MySpider(scrapy.spider.Spider):
    name = 'spider_jobui'
    CityInfoList = []
    cur = 0
    baseUrl = "http://www.jobui.com"
    def start_requests(self):
        yield scrapy.Request(url='http://www.jobui.com/salary/hainan/', callback=self.setCityUrlAndNameList,dont_filter=True)
    def parse(self,response):
        self.cur += 1
        sel = Selector(response)
        item = JobuiItem()
        item['citySpell'] = response.url[:-1].split('/')[-1]  #/salary/hefei/
        item['city'] = sel.xpath("//div[@class='aleft']/h1[@class = 'headTitle']/text()").extract()[0].split('平均工资'.decode('utf-8'))[0]
        item['dateTime'] = sel.xpath("//div[@class='aleft']/div[@class='jk-box ']/div/div/div/text()").extract()[3].strip().split()[1][:-1]
        item['sampleSize'] = sel.xpath("//div[@class='aleft']/div[@class='jk-box ']/div/div/div/a/strong/text()").extract()[0]
        item['salary'] = sel.xpath("//div[@class='aleft']/div[@class='jk-box ']/div/div/div/strong/text()").extract()[0][1:]
        yield item

        if self.cur < len(self.CityInfoList) - 1:
            yield scrapy.Request(url=self.baseUrl +self.CityInfoList[self.cur],callback=self.parse,dont_filter=True)

    def setCityUrlAndNameList(self,reponse):
        sel = Selector(reponse)
        cityInfoSelList =  sel.xpath("//div[@class = 'ui-changeArea']/ul/li/p/a").extract()
        self.CityInfoList = [ Selector(text=cityInfo,type = "html").xpath("//a/@href").extract()[0]for cityInfo in cityInfoSelList]
        yield scrapy.Request(url=self.baseUrl +self.CityInfoList[self.cur],callback=self.parse,dont_filter=True)

