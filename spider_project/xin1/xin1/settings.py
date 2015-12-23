# -*- coding: utf-8 -*-

# Scrapy settings for xin1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'xin1'

SPIDER_MODULES = ['xin1.spiders']
NEWSPIDER_MODULE = 'xin1.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xin1 (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['xin1.pipelines.Xin1Pipeline', ]
MONGODB_SERVER = "10.138.30.34"
MONGODB_PORT = 27017
MONGODB_DB = "blacklist"
MONGODB_COLLECTION = "xin1"