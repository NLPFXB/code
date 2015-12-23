# -*- coding: utf-8 -*-

# Scrapy settings for nbcredit project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'nbcredit'

SPIDER_MODULES = ['nbcredit.spiders']
NEWSPIDER_MODULE = 'nbcredit.spiders'
ITEM_PIPELINES = ['nbcredit.pipelines.NbcreditPipeline', ]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nbcredit (+http://www.yourdomain.com)'
MONGODB_SERVER = "10.138.30.34"
MONGODB_PORT = 27017
MONGODB_DB = "blacklist"
MONGODB_COLLECTION = "nbcredit"