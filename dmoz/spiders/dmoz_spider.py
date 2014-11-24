import string, scrapy
from scrapy import Spider
from scrapy.selector import Selector
from dmoz.items import DmozItem

# This class defines the rules according to which we extract information
# from the urls we scrape
class DmozSpider(Spider):
        name = "dmoz"
        allowed_domains = ["dmoz.org"]

        # the urls we want to scrape
        start_urls = [
                "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
                "http://www.dmoz.org/Computers/Programming/Languages/JavaScript/Books/",
                "http://www.dmoz.org/Computers/Programming/Languages/Ruby/Books/",
                "http://www.dmoz.org/Computers/Programming/Languages/Lisp/Books/",
                "http://www.dmoz.org/Computers/Programming/Languages/Eiffel/Books/"
                ]

        langs = ['python', 'javascript', 'ruby', 'lisp', 'eiffel']
        max_title_length = 150
        max_desc_length = 500

        def get_title(self, raw_title):
            """Given the raw title returns a better string representation"""

            title = " ".join("".join(raw_title).split()).strip()

            if len(title) > self.max_title_length:
                return title[:self.max_title_length-3] + "..."

            return title[:self.max_title_length]

        def get_desc(self, raw_desc):
            """Given the raw description returns a better string representation"""

            desc = " ".join("".join(raw_desc).split()).strip()

            # removes the " - " substring existing in the beggining of the description
            desc = desc[2:self.max_desc_length]

            if len(desc) > self.max_desc_length:
                return title[:self.max_desc_length-3] + "..."

            return desc[:self.max_desc_length]

        def get_category(self, url):
            """Given the start url returns the programming language the book is written about"""

            category = [lang for lang in self.langs if lang in url.lower()]
            return category[0] if len(category) > 0 else "unknown"

        def parse(self, response):
            sel = Selector(response)
            scrapped_items = sel.xpath('//ul[@class="directory-url"]/li')
            result = []

            for item in scrapped_items: 
                dmoz_item = DmozItem()
                dmoz_item['title'] = self.get_title(item.xpath('a/text()').extract())
                dmoz_item['desc'] = self.get_desc(item.xpath('text()').extract())
                dmoz_item['category'] = self.get_category(response.request.url)

                result.append(dmoz_item)

            return result

