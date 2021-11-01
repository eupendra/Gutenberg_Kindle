BOT_NAME = 'kindle'

SPIDER_MODULES = ['kindle.spiders']
NEWSPIDER_MODULE = 'kindle.spiders'
ITEM_PIPELINES = {'kindle.pipelines.CustomDownloadPipeline': 1}
FILES_STORE = 'downloads'
MEDIA_ALLOW_REDIRECTS = True



# Obey robots.txt rules
ROBOTSTXT_OBEY = False

AUTOTHROTTLE_ENABLED = False