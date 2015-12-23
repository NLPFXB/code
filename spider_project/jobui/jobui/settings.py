# -*- coding: utf-8 -*-

# Scrapy settings for jobui project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jobui'

SPIDER_MODULES = ['jobui.spiders']
NEWSPIDER_MODULE = 'jobui.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jobui (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['jobui.pipelines.JobuiPipeline', ]
MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "blacklist"
MONGODB_COLLECTION = "jobui"