__author__ = 'fengxiaobo'
import scrapy
import json
from zhixing.items import ZhixingItem
import pymongo
from pymongo import MongoClient
import requests
import PyV8
import re
import time
import urllib2
def get_begin_number():
    ret = 1
    client = MongoClient('localhost',27017)
    download_delay = 1
    db = client['blacklist']
    collection = db['zhixing']
    for item in collection.find().sort('id',pymongo.DESCENDING).limit(1):
        ret = int(item['id'])
    return ret
class mySpider(scrapy.spider.Spider):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"}
    name = 'zhixing_spider'
    begin = 3892164
    MAX = 100000000
    origin_url = 'http://zhixing.court.gov.cn/search/detail?id='
    allowed_domains=["zhixing.court.gov.cn"]

    def start_requests(self):
        url = self.origin_url+str(self.begin)
        cookies = self.getCookies(url)
        return [scrapy.Request(url = url , callback = self.parser, dont_filter=True ,headers = self.headers ,cookies =cookies)]
    def parser(self,response):
        if '<script>' in response.body:
            url = response.url
            cookies = self.getCookies(url)
            body = requests.get(url = url, headers = self.headers, cookies = cookies).text
        else:
            body = response.body
        try:
            items = json.loads(body)
            item = ZhixingItem()
            item["id"] = items["id"]
            item["caseCode"] = items["caseCode"]
            item["caseState"] = items["caseState"]
            item["execCourtName"] = items["execCourtName"]
            item["execMoney"] = items["execMoney"]
            item["partyCardNum"] = items["partyCardNum"]
            item["pname"] = items["pname"]
            item["caseCreateTime"] = items["caseCreateTime"]
            yield item
        except Exception as e:
            pass
        if self.begin < self.MAX:
            self.begin += 1
            nex_url = self.origin_url + str(self.begin)
            next_cookies = self.getCookies(nex_url)

            yield scrapy.Request(url= nex_url, callback= self.parser,dont_filter=True ,headers = self.headers, cookies =next_cookies)

    def getFirstHtml(self,url):
        try:
            html = requests.get(url=url, headers = self.headers)
        except:
            flag = True
            while flag:
                try:
                    html = requests.get(url=url, headers = self.headers)
                    flag = False
                except:
                    print html,html.text
                    time.sleep(10)
        return html
    def getFirstCookies(self,html):
        return html.cookies._cookies
    def getJsluid(self,html):
        firstCookies = self.getFirstCookies(html)
        jsluid = str(firstCookies['zhixing.court.gov.cn']['/']['__jsluid']).split()[1].split('=')[1]
        return jsluid
    def getFirstHtmlContent(self,html):
        return html.text
    def getJSRunResult(self,html):
        html = self.getFirstHtmlContent(html)
        functionBegin = html.index('(function(a){eval(function(p,a,c,k,e,d)')
        functionEnd = html.index(');return p;}')
        functionBody = 'function test(p,a,c,k,e,d)'+html[functionBegin+39:functionEnd+12]+';'
        params = html[functionEnd+12:]
        p = re.compile(r";',(\d+),(\d+),'\|")
        res = p.search(html).group()
        paramP = "var p = "+ params[1:params[1:].index(res)+3] +";"
        paramA = "var a = " + p.findall(html)[0][0]+";"
        paramC = "var c = " + p.findall(html)[0][1]+";"
        params = params.split(res[:-2])[1]
        paramKIndexEnd = params.index(',0,{}));})')
        paramK = "var k = "+ params[:paramKIndexEnd]+";"
        paramE = "var e = 0 ;"
        paramD = "var d = {};"
        newParam = functionBody+paramP+paramA+paramC+paramK+paramE+paramD +'test(p,a,c,k,e,d);'
        ctxt = PyV8.JSContext()
        ctxt.enter()
        func = ctxt.eval(newParam)
        func = func[:func.rindex('setTimeout("lo')]
        preRun = "var dc=\"\";var t_d={hello:\"world\",t_c:function(x){if(x===\"\")return;if(x.slice(-1)===\";\"){x=x+\" \";};if(x.slice(-2)!==\"; \"){x=x+\"; \";};dc=dc+x;}};"
        a2 = params.split('0,{}));})(')[1]
        paramA2 = "var a = "+a2[:a2.rindex(';document.cookie')-1]+";"
        allFunction = "(function(){" + preRun + paramA2 + func + "return dc })"
        func = ctxt.eval(allFunction)
        res = func().split(';')[0]#__jsl_clearance=1448948882.413|0|vMuEK%2F2YtIOLddxT5kiyniI0yDA%3D
        return res
    def getCookies(self,url):
        html = self.getFirstHtml(url)
        id = self.getJsluid(html)
        try:
            jsl_clearance = self.getJSRunResult(html).split('=')[1]
        except:
            with open('1.txt','w') as f:
                f.write(html.text.decode('utf-8'))
        return  dict(__jsluid = id , __jsl_clearance = jsl_clearance)
