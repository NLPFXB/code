#coding:utf-8
__author__ = 'fengxiaobo'
import scrapy
from nbcredit.items import NbcreditItem
import re
import math
class nbcreditSpider(scrapy.spider.Spider):
    name = 'nbcreditSpiders'
    # download_delay = 1
    allowed_domains=["www.nbcredit.net"]
    start_urls = ['http://www.nbcredit.net/zx/gjcx/gjcxinit.shtml?dispatch=getfyzxajbymc2']
    params_dict = {"MC	":"","SFZ":"","limit2":"30","start2":"1"}
    current_page = 1
    def parse(self,response):
        person_list = re.findall(r'							var (.*?).append\(formatstr2\);',response.body,re.S)
        s = re.findall(r'total2=\d+?;',response.body)
        total = int(re.compile(r'\d+').findall(s[0])[1])
        page_num = math.ceil(float(total)/float(30))
        if self.current_page < page_num:
            item = NbcreditItem()
            for person in person_list:
                temp_lit = person.split('\n')
                for line in temp_lit:
                    if '(\"_TITLE_\",' in line:
                        item['name'] = line.split('\"_TITLE_\",\"')[-1][:-4]
                    if "(\"_SFZ_\"" in line:
                        item['cardIDnum']=line.split('(\"_SFZ_\",\"')[-1][:-4]
                yield item
            url = response.url
            t = scrapy.FormRequest(url=url,formdata=self.params_dict,callback=self.parse)
            self.params_dict['start2']=str(self.current_page+1)
            self.current_page+=1
            yield t



