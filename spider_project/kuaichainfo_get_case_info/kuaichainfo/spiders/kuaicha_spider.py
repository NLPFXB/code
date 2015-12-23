#coding:utf8
__author__ = 'fengxiaobo'
'''
老赖网黑名单爬取
'''
import scrapy
import json
from kuaichainfo.items import KuaichainfoItem
import httplib,urllib
import cookielib,urllib2
class kuaicha_spider(scrapy.spider.Spider):
    download_delay = 1
    # headers = {'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate',
    #        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3','Cache-Control':'no-cache','Connection':'keep-alive',
    #       'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #        'Cookie':"Hm_lvt_1a3be0237a9f27b5917d61502bf49f6d=1438759469,1438821898,1439187574,1439262685; JSESSIONID=CB1BEB64F68E060EE6B62BC27F8DEE3C\
    #        ; Hm_lpvt_1a3be0237a9f27b5917d61502bf49f6d=1439262751; creditAccessId=0bd0e76b8e963958b11968cf2b5cb6bde2eff6a7fd5435546e32154aeeb81f599f8458bed06c9969\
    #        ; creditAppKey=e1564875b4e01147dfdee18737619dd0704f98532606e2312c21ab1cf133aeaf; creditAppName=af213c950fa82a7a9a0440105c630058\
    #        ; creditDeviceID=9190c13c78fb927489317aa2729d52e3f15a5902290bd8bc0045a81f3c794a128b9fe89923f7f9e5",
    #        'Host':'www.kuaicha.info','Pragma':'no-cache','Referer':'http://www.kuaicha.info/lawMobile/lawArea.jsp?ip=yes','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
    #        'X-Requested-With':'XMLHttpRequest'}
    params_dict={'accessId':'0bd0e76b8e963958b11968cf2b5cb6bde2eff6a7fd5435546e32154aeeb81f599f8458bed06c9969',
                           'pageSize':'20','province':'上海省','startIndex':'20'}
    # params_person = urllib.urlencode()
    #conn = httplib.HTTPConnection('www.kuaicha.info')
    name =  'kuaicha'
    allowed_domains = ['http://www.kuaicha.info']
    start_urls = ['http://www.kuaicha.info/lawMobile/law.html']
    #删除了'北京','上海', '天津',
    province_list = ['重庆','四川','贵州', '云南','西藏','河南','湖北','湖南','广东','广西','陕西','甘肃','青海','宁夏','新疆','河北','山西',
                     '内蒙古', '江苏', '浙江', '安徽', '福建', '江西', '山东', '辽宁', '吉林','黑龙江','海南']
    def parse(self, response):
        for province in self.province_list:
            self.params_dict['province'] = province
            i = 0
            flag = True
            while flag :
                self.params_dict['startIndex'] = str(i)
                print self.params_dict['province'].decode('utf8')
                params_person = urllib.urlencode(self.params_dict)
                perspon_list = self.get_post(params_person)
                if not perspon_list:
                    flag = perspon_list
                    break
                for perspon_info in perspon_list:
                    item = KuaichainfoItem()
                    item['name'] = perspon_info[0]
                    item['area'] = perspon_info[1]
                    item['cardNum'] = perspon_info[2]
                    item['case'] = perspon_info[3]
                    yield item
                i+=20
    def get_post(self,params):
        flag = True
        while flag:
            try:
                t = self._get_post(params)
            except IndexError,e:
                flag = False
                return False
            except Exception,e:
                print e
                pass
        return t
    def _get_post(self,params):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        f = opener.open('http://www.kuaicha.info/')
        user_agent = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"}
        url = 'http://www.kuaicha.info/findExecutedPersonListByArea.action'
        req = urllib2.Request(url,headers = user_agent,data=params)
        content = urllib2.urlopen(req)
        res = opener.open(req)
        jsonstring = json.loads(res.read())
        persion_information_list = []
        persion_information = []
        for i in range(0,20):
            persion_information.append(jsonstring['data']['areaList'][i]['name']) #姓名
            persion_information.append(jsonstring['data']['areaList'][i]['area']) #户籍区域
            persion_information.append(jsonstring['data']['areaList'][i]['cardNum']) #身份证号码
            case_list = jsonstring['data']['areaList'][i]['classPersonJson']
            case_dict = {}
            for j in range(len(case_list)):
                case_list[j]['caseType'] = str(case_list[j]['caseType'])
                case_dict[str(j)] = case_list[j]
                for key in case_list[j].keys():
                    case_list[j][key] = case_list[j][key].encode('utf8') #要将key值转换成utf-8编码
                params = urllib.urlencode( case_list[j])
                url  = 'http://www.kuaicha.info/getExecutedPersonDetail.action'
                req = urllib2.Request(url,headers=user_agent,data=params)
                res = opener.open(req)
                case_dict_temp = json.loads(res.read())['data']
                for  key in case_dict_temp.keys():
                    if type(case_dict_temp[key])== int:
                        if case_dict_temp[key]==0:
                            case_dict_temp.pop(key)
                    elif type(case_dict_temp[key])== str:
                        if len(case_dict_temp[key])==0:
                            case_dict_temp.pop(key)
                    else:
                        if not case_dict_temp[key]:
                            case_dict_temp.pop(key)
                if 'caseType' in case_dict_temp.keys():
                    case_dict_temp.pop('caseType')
                if 'caseId' in case_dict_temp.keys():
                    case_dict_temp.pop('caseId')
                case_dict[str(j)].update(case_dict_temp)
                if 'caseType' in case_dict[str(j)].keys():
                    case_dict[str(j)].pop('caseType')
                if 'caseId' in case_dict[str(j)].keys():
                    case_dict[str(j)].pop('caseId')
            persion_information.append(case_dict) #案件详情
            persion_information_list.append(persion_information)
            persion_information = []
        return persion_information_list

