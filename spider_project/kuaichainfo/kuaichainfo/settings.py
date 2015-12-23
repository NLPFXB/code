# -*- coding: utf-8 -*-

# Scrapy settings for kuaichainfo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kuaichainfo'

SPIDER_MODULES = ['kuaichainfo.spiders']
NEWSPIDER_MODULE = 'kuaichainfo.spiders'
COOKIES_ENABLED = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kuaichainfo (+http://www.yourdomain.com)'
ITEM_PIPELINES = ['kuaichainfo.pipelines.KuaichainfoPipeline', ]
MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "mydb"
MONGODB_COLLECTION = "kuaicha"