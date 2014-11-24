BOT_NAME = 'dmoz'

SPIDER_MODULES = ['dmoz.spiders']
NEWSPIDER_MODULE = 'dmoz.spiders'


ITEM_PIPELINES = {'dmoz.pipeline.DmozPrunePipeline': 1,
                  'dmoz.store_pipeline.ItemsToPostgres': 2}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'dmoz (+http://www.yourdomain.com)'

DB_NAME = 'scrapeDB'
DB_USER = 'testuser'
DB_PASSWD = 'test'
DB_HOST = 'localhost'
