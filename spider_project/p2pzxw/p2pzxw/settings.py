# -*- coding: utf-8 -*-

# Scrapy settings for p2pzxw project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'p2pzxw'

SPIDER_MODULES = ['p2pzxw.spiders']
NEWSPIDER_MODULE = 'p2pzxw.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'p2pzxw (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['p2pzxw.pipelines.P2PzxwPipeline', ]
MONGODB_SERVER = "10.138.30.34"
MONGODB_PORT = 27017
MONGODB_DB = "blacklist"
MONGODB_COLLECTION = "p2pzxw"