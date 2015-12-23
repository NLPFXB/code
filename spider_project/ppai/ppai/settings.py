# -*- coding: utf-8 -*-

# Scrapy settings for ppai project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ppai'

SPIDER_MODULES = ['ppai.spiders']
NEWSPIDER_MODULE = 'ppai.spiders'
COOKIES_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ppai (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['ppai.pipelines.PpaiPipeline', ]

MONGODB_SERVER = "10.138.30.34"
MONGODB_PORT = 27017
MONGODB_DB = "blacklist"
MONGODB_COLLECTION = "ppai"