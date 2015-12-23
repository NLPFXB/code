# -*- coding: utf-8 -*-

# Scrapy settings for zhixing project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhixing'

SPIDER_MODULES = ['zhixing.spiders']
NEWSPIDER_MODULE = 'zhixing.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhixing (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['zhixing.pipelines.ZhixingPipeline', ]
MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "blacklist"
MONGODB_COLLECTION = "zhixing"