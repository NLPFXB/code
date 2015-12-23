# -*- coding: utf-8 -*-

# Scrapy settings for zhengxingSystem project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhengxingSystem'

SPIDER_MODULES = ['zhengxingSystem.spiders']
NEWSPIDER_MODULE = 'zhengxingSystem.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhengxingSystem (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['zhengxingSystem.pipelines.ZhengxingsystemPipeline', ]
MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "blacklist"
MONGODB_COLLECTION = "zhengxingSystem"
COOKIES_ENABLED = False
