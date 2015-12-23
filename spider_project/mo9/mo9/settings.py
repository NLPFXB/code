# -*- coding: utf-8 -*-

# Scrapy settings for mo9 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mo9'
COOKIES_ENABLED = False
SPIDER_MODULES = ['mo9.spiders']
NEWSPIDER_MODULE = 'mo9.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mo9 (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['mo9.pipelines.Mo9Pipeline', ]
MONGODB_SERVER = "10.138.30.34"
#MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "blacklist"
#MONGODB_DB = "mydb"
MONGODB_COLLECTION = "mo9"

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
# USER_AGENTS = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
# ]
#
#
#
# DOWNLOADER_MIDDLEWARES = {
# #    'cnblogs.middlewares.MyCustomDownloaderMiddleware': 543,
#     'mo9.middlewares.RandomUserAgent': 1,
#     # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#     # 'mo9.middlewares.ProxyMiddleware': 100,
# }

# import urllib2
# import re
# from bs4 import BeautifulSoup
# url_list = ['http://www.xicidaili.com/nt']
# #,'http://www.xicidaili.com/nt/2'
#
# def getContent(url):
#     headers = {'User-Agent':'<a href="https://www.baidu.com/s?wd=Mozilla&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1Ydnjn4Pyf3mWf1myD3mHwW0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1cknHTzPjcsn1cYrHm3nHm1njT" target="_blank" class="baidu-highlight">Mozilla</a>/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#     req = urllib2.Request(url,headers = headers)
#     myResponse  = urllib2.urlopen(req)
#     html = BeautifulSoup(myResponse,"lxml")
#     return html
# def get_proxies_dict(url):
#     html = getContent(url)
#     result = []
#     proxies_dict = {}
#     pattern = re.compile(r"<div class=\"bar_inner (.*?)\"")
#     for line in html.select('tr[class]'):
#         if pattern.findall(str(line))[0] == pattern.findall(str(line))[1] == 'fast':
#             proxies_dict['ip_port'] = line.text.strip().split()[0].encode('utf-8') + ':' + line.text.strip().split()[1].encode('utf-8')
#             result.append(proxies_dict)
#     return result
#
# def get_all_proxies_dict(url_list):
#     result = map(get_proxies_dict,url_list)
#     res = []
#     for line in result:
#         res.extend(line)
#     return res
#
# # PROXIES = get_all_proxies_dict(url_list)
# PROXIES = [{'ip_port':'124.240.187.89:82'}]
