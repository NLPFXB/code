#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
from bs4 import BeautifulSoup
import urllib2
from p2pzxw.items import P2PzxwItem
from scrapy.selector import Selector

def getPageTotalNum(url):
    '''
    :param url: 网址
    :return: 得到总页数
    '''
    pageTotalNum = 0
    html = getContent(url)
    pageHtmlList = html.find_all("form")
    for page in pageHtmlList:
        if page.attrs.has_key('method'):
            pageTotalNum = getNum(page)
    return pageTotalNum
def getNum(html):
    num = 0
    htmlText = html.text
    htmlText = htmlText.replace("\r","")
    # '\n'.join([line.strip() for line in htmlText.encode('utf-8').split('\n') if line])
    for line in htmlText.encode('utf-8').split('\n'):
        if '页次' in line:
            num = int(line.split('/')[1][:-3]) #-3是因为utf-8编码“页”字是三个字符位
    return num
def getContent(url):
    headers = {'User-Agent':'<a href="https://www.baidu.com/s?wd=Mozilla&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1Ydnjn4Pyf3mWf1myD3mHwW0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1cknHTzPjcsn1cYrHm3nHm1njT" target="_blank" class="baidu-highlight">Mozilla</a>/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url,headers = headers)
    myResponse  = urllib2.urlopen(req)
    html = BeautifulSoup(myResponse,"lxml")
    return html

class p2pSpider(scrapy.spider.Spider):
    originUrl = 'http://www.p2pzxw.com/'
    pageTotalNum = getPageTotalNum(originUrl)#得到总页数

    download_delay = 1
    name = 'p2pzxwSpider'
    allowed_domains = ["p2pzxw.com"]
    start_urls = [("http://www.p2pzxw.com/index.asp?Page="+str(i)) for i in range(1,pageTotalNum+1)]

    def parse(self,response):
        sel = Selector(response)

        for line in sel.xpath("//div[@class='yqsj_kk']").extract():
            itemsList = self.getPageItem(line)

            item = P2PzxwItem()
            item['name'] = itemsList[1].split('：')[1].strip()
            item['cardNum'] = itemsList[2].split('：')[1].strip()
            item['sex'] = itemsList[3].split('：')[1].strip()
            item['cardAddress'] = itemsList[4].split('：')[1].strip()
            item['homeAddress'] = itemsList[5].split('：')[1].strip()
            item['contactNumber'] = itemsList[6].split('：')[1].strip()
            item['ArrearsTotal'] = self.getNumFromPage(itemsList[7].split('：')[1].strip())
            item['TotalPenalty'] = itemsList[8].split('：')[1].strip()
            item['OverdueNum'] = self.getNumFromPage(itemsList[9].split('：')[1].strip())
            item['websiteNum'] = self.getNumFromPage(itemsList[10].split('：')[1].strip())
            item['OverdueDays'] = self.getNumFromPage(itemsList[11].split('：')[1].strip())
            item['updateTime'] = itemsList[12].split('：')[1].strip()

            if item['cardNum'].isdigit():
                yield item

    def getPageItem(self,html):
        bsHtml = BeautifulSoup(html)
        text = [ line.strip() for line in bsHtml.text.encode('utf-8').split('\n') if line ]
        return text

    def getNumFromPage(self,containNumString):
        numList = [numString for numString in containNumString if numString.isdigit()]
        numString = ''.join(numList)
        if numString:
            return int(''.join(numList))
        return ''

