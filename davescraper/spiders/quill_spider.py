import scrapy
from scrapy.loader import ItemLoader
from davescraper.items import QuillItem


class QuillSpider(scrapy.Spider):
    name = 'quill'
    allowed_domains = ["quill.com"]
    start_urls = [
        'https://www.quill.com/search?keywords=Gel+Pens'
    ]

    def __init__(self):
        super(QuillSpider, self).__init__()
        pass

    # def start_requests(self):
    #     url = self.start_urls[0]
    #     yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        items = response.css('div#ResultsSection div.BrowseItem')
        for item in items:
            loader = ItemLoader(item=QuillItem(), selector=item)
            loader.add_css('title', 'h3#skuName a::text')
            loader.add_css('price', 'span#SkuPriceUpdate::text')
            loader.add_css('number', 'div#ItemSrchCompare div.iNumber::text')

            yield loader.load_item()

        next_page_string = response.css('div#Pager span.next::attr(data-querystring)').get()
        next_page = 'search?' + next_page_string

        if next_page is not None:
            next_page = response.urljoin(next_page)
            self.logger.info('Next Page : {}'.format(next_page))
            yield scrapy.Request(next_page, callback=self.parse)



