# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from  scrapy.conf import settings
from  scrapy.exceptions import DropItem
from  scrapy import  log

class JobuiPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")
        self.collection.update({'city': item['city']},dict(item), upsert=True)
        #self.collection.insert(dict(item))
        log.msg("Question added to MongoDB database!",
                level=log.DEBUG, spider=spider)
        return item