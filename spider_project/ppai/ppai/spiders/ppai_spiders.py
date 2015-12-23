#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
from bs4 import BeautifulSoup
import urllib2
from ppai.items import PpaiItem
from scrapy.http import Request
from scrapy.selector import  Selector
class get_url_Page(object):
    '''
    从首页地址获取尾页的地址以及年份
    '''
    def __init__(self,url):
        self.url = url
    def _getContent(self,url):
        headers = {'User-Agent':'<a href="https://www.baidu.com/s?wd=Mozilla&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1Ydnjn4Pyf3mWf1myD3mHwW0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1cknHTzPjcsn1cYrHm3nHm1njT" target="_blank" class="baidu-highlight">Mozilla</a>/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request(url,headers = headers)
        myResponse  = urllib2.urlopen(req)
        html = BeautifulSoup(myResponse,"lxml")
        return html
    def get_tail_num(self):
        return  self.parse_html()[0]
    def get_years_list(self):
        return self.parse_html()[1]
    def parse_html(self):
        '''
        :return: 解析html网页，得到尾页数字和年份列表
        '''
        years_list = []
        tail_num = 0
        html = self._getContent(self.url)
        for line in html.find_all("div"):
            if 'class' in line.attrs and line['class'] == ['tit_nav']:
                   years_list.extend(line.get_text().split()[:-1])
            if 'class' in line.attrs and line['class'] == ['fen_ye_nav']:
               try:
                   tail_num = int(line.get_text().split('共'.decode('utf8'))[1][:-1])
               except:
                   pass
        return tail_num,years_list
def get_start_urls():
    start_urls = []
    start_url_page = get_url_Page('http://www.ppdai.com/blacklist/2015')
    years_list =start_url_page.get_years_list()
    for year in years_list:
        url_page = get_url_Page("http://www.ppdai.com/blacklist/"+str(year))
        tail_num = url_page.get_tail_num()
        url = "http://www.ppdai.com/blacklist/"+str(year)+"_m0_p"
        urls = [url+str(i) for i in range(tail_num+1)]
        start_urls.extend(urls)
    return  start_urls
class ppdaiSpider(scrapy.spider.Spider):
    name = "ppdai"
    allowed_domains=["www.ppdai.com"]
    download_delay = 1
    start_urls = get_start_urls()
    def parse(self,response):
        orgin_url = 'http://www.ppdai.com'
        sel = Selector(response)
        if 'blacklistdetail' in response.url:
            item = PpaiItem()
            user_data = sel.xpath('//ul//li/text()').extract()
            user_data = [line.strip() for line in  user_data if len(line.strip()) > 1]
            for data in user_data:
                if '用户名'.decode('utf8') in data:
                    item['user_name'] = data[4:]
                if '姓名'.decode('utf8') in data:
                    item['peron_name'] = data[3:]
                if '手机号'.decode('utf8') in data:
                    item['mobilephone_number'] = data[4:]
                if '身份证号'.decode('utf8') in data:
                    item['identitycard'] = data[5:]
            about_money_data = sel.xpath('//tr/td/text()').extract()
            item['own_Money'] = about_money_data[0][8:]
            item['borrow_period'] = about_money_data[-5]
            item['borrow_time'] = about_money_data[-4]
            item['over_days'] = about_money_data[-3]
            item['overduecharge'] = about_money_data[-2][1:]
            yield item
        urls = sel.xpath('//input/@onclick').extract()
        for url in urls:
            url = orgin_url + url.split("='")[1][:-1].strip()
            yield Request(url, callback=self.parse)


