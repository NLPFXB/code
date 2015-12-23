#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from tutorial.items import DmozITem
from bs4 import BeautifulSoup
import chardet
import urllib2
import codecs
class DmozSpider(scrapy.spider.Spider):
    name = "ppdai"
    allowed_domains=["www.ppdai.com"]
	#减慢爬取速度 为1s
    download_delay = 1
    start_urls=['http://www.ppdai.com/blacklist/2015_m0_p'+str(x) for x in range(1,58)]
    def parse(self, response):
        sel = Selector(response)
        #获取黑名单的名字和信息
        origin_url = 'http://www.ppdai.com'
        item  = DmozITem()
        filename = response.url.split('_p')[-1]
        urls = [(origin_url+url.split("='")[-1][:-1].strip()) for url in sel.xpath('//input/@onclick').extract()]
        item['urls'] = urls
        #使用map函数
        user_name_list = map(self.get_ban_username,urls)
        self.download_name(filename,'\n'.join(user_name_list))
    def download_name(self,filename,html):
        with codecs.open(filename+".txt",'w',encoding='utf-8') as f:
            f.write(html)
    def get_content_url(self,url):
        headers = {'User-Agent':'<a href="https://www.baidu.com/s?wd=Mozilla&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1Ydnjn4Pyf3mWf1myD3mHwW0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1cknHTzPjcsn1cYrHm3nHm1njT" target="_blank" class="baidu-highlight">Mozilla</a>/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request(url,headers = headers)
        myResponse  = urllib2.urlopen(req)
        html = BeautifulSoup(myResponse,"lxml")
        return html
    def get_ban_username(self,url):
        html = self.get_content_url(url)
        write = ''
        for line in html.find_all('div'):
            if 'class' in line.attrs and line['class'] == ['blacklist_detail_nav']:
                if '曝光资料'.decode('utf8') in line.get_text():
                    temp = line.get_text()
                    temp = '\n'.join([line for line in temp.replace(' ','').split('\n') if len(line)>1])
                    write += temp
        return write

    def download(self,content_tuple):
        url = content_tuple[0]
        filename = content_tuple[1]
        self.download_name(filename,self.get_ban_username(self.get_content_url(url)))
