# -*- coding: utf-8 -*-

# Scrapy settings for kaikaidai project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kaikaidai'

SPIDER_MODULES = ['kaikaidai.spiders']
NEWSPIDER_MODULE = 'kaikaidai.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kaikaidai (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['kaikaidai.pipelines.KaikaidaiPipeline', ]
MONGODB_SERVER = "10.138.30.34"
MONGODB_PORT = 27017
MONGODB_DB = "blacklist"
MONGODB_COLLECTION = "kaikaidai"