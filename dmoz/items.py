import scrapy

"""
This class contains the item information we would like to maintain. That
is the title, the description and the category of the item (i.e. book).
"""

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()

    """Python, javascript, etch"""
    category = scrapy.Field()
