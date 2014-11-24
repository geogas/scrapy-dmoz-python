from scrapy.exceptions import DropItem

# This class filters the scraped results, items
# containing certain words are ruled out
class DmozPrunePipeline(object):
    words_to_filter  = ['Java']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['title']).lower():
                raise DropItem("Bad: ", item['title'])
            else:
                return item
