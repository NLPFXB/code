#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
from bs4 import BeautifulSoup
class mySpider(scrapy.spider.Spider):
    name = 'spiderMy089'
    start_urls = ['https://www.my089.com/Loan/BlackList.aspx?Time=all']

    def parse(self,response):
        with open('1.txt','w') as f:
            f.write(response.body)

