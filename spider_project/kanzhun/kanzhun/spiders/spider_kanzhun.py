#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
import time
import json
import base64
import urllib
class spider_kanzhun(scrapy.spider.Spider):
    headers = {'Content-Type':'application/x-www-form-urlencoded',
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
               }
    proxy_ip_port = ''
    download_delay = 5
    name = 'kanzhun_spider'
    allowed_domains = ['kanzhun.com']
    start_urls = ['http://www.kanzhun.com/xsa1p1.html?ka=salary-rankcity1']
    def start_requests(self):
        params ={'account':'wode701@163.com','password':'t117842909','redirect':'http://www.kanzhun.com/'}
        return [scrapy.Request("http://www.kanzhun.com/login.json",method='post',headers=self.headers,
                               body=urllib.urlencode(params),callback=self.post_login)]
    def post_login(self,response):

        print '=================================='
        print json.loads(response.body)['resmsg']
        print 'start login'
        # return [scrapy.FormRequest.from_response(response,formdata = params,callback = self.after_login, headers = self.headers)]
    def after_login(self,response):
        print '=================================='
        print 'loading compelte'
