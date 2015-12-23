#coding:utf8
__author__ = 'fengxiaobo'
'''
老赖网黑名单爬取
'''
import scrapy,json
import urllib2,urllib,cookielib
from kuaichainfo.items import KuaichainfoItem
class kuaicha_spider(scrapy.spider.Spider):
    download_delay = 1
    headers = {'User-Agent': '	Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'}
    params_dict={'accessId':'0bd0e76b8e963958b11968cf2b5cb6bde2eff6a7fd5435546e32154aeeb81f599f8458bed06c9969',
                           'pageSize':'20','province':'上海省','startIndex':'20'}
    name =  'kuaicha'
    # allowed_domains = ['http://www.kuaicha.info']
    start_urls = ['http://www.kuaicha.info/']
    province_list = ['北京','上海', '天津','重庆','四川','贵州', '云南','西藏','河南','湖北','湖南','广东','广西','陕西','甘肃','青海','宁夏','新疆','河北','山西',
                     '内蒙古', '江苏', '浙江', '安徽', '福建', '江西', '山东', '辽宁', '吉林','黑龙江','海南']
    def start_requests(self):
        return [scrapy.Request('http://www.kuaicha.info/lawMobile/lawArea.jsp?p=%E5%9B%9B%E5%B7%9D&c=null', meta = {'cookiejar' : 1},callback = self.post_province,method='GET')] #删除了,
    def post_province(self,response):
        #获取上一个网址的cookies，然后以后的每一个访问都有cookies
        # print response.meta['cookiejar']
        # print response.cookies
        print '===================='
        yield scrapy.Request(url ='http://www.kuaicha.info/findExecutedPersonListByArea.action',headers=self.headers,
                                 body=urllib.urlencode(self.params_dict),callback=self.parse_province_data,method='POST',meta = {'cookiejar' : response.meta['cookiejar']})#
    def parse_province_data(self,response):
        print '====================================='
        print json.loads(response.body_as_unicode())
        print '====================================='


    # def parse(self, response):
    #     for province in self.province_list:
    #         self.params_dict['province'] = province
    #         i = 0
    #         flag = True
    #         while flag :
    #             self.params_dict['startIndex'] = str(i)
    #             print i
    #             print self.params_dict['province'].decode('utf8')
    #             params_person = urllib.urlencode(self.params_dict)
    #             perspon_list = self.get_post(params_person)
    #             if not perspon_list:
    #                 flag = perspon_list
    #                 break
    #             for perspon_info in perspon_list:
    #                 item = KuaichainfoItem()
    #                 item['name'] = perspon_info[0]
    #                 item['area'] = perspon_info[1]
    #                 item['cardNum'] = perspon_info[2]
    #                 item['case'] = perspon_info[3]
    #                 yield item
    #             i+=20
    # def get_post(self,params):
    #     flag = True
    #     while flag:
    #         try:
    #             t = self._get_post(params)
    #         except IndexError,e:
    #             flag = False
    #             return False
    #         except Exception,e:
    #             print e
    #             pass
    #     return t
    # def _get_post(self,params):
    #     cookie = cookielib.CookieJar()
    #     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    #     f = opener.open('http://www.kuaicha.info/')
    #     user_agent = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"}
    #     url = 'http://www.kuaicha.info/findExecutedPersonListByArea.action'
    #     req = urllib2.Request(url,headers = user_agent,data=params)
    #     content = urllib2.urlopen(req)
    #     res = opener.open(req)
    #     jsonstring = json.loads(res.read())
    #     persion_information_list = []
    #     persion_information = []
    #     for i in range(0,20):
    #         persion_information.append(jsonstring['data']['areaList'][i]['name']) #姓名
    #         persion_information.append(jsonstring['data']['areaList'][i]['area']) #户籍区域
    #         persion_information.append(jsonstring['data']['areaList'][i]['cardNum']) #身份证号码
    #         case_list = jsonstring['data']['areaList'][i]['classPersonJson']
    #         case_dict = {}
    #         for j in range(len(case_list)):
    #             case_list[j]['caseType'] = str(case_list[j]['caseType'])
    #             case_dict[str(j)] = case_list[j]
    #         persion_information.append(case_dict) #案件详情
    #         persion_information_list.append(persion_information)
    #         persion_information = []
    #     return persion_information_list

