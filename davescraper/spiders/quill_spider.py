import scrapy
from scrapy.loader import ItemLoader
from davescraper.items import QuillItem


class QuillSpider(scrapy.Spider):
    name = 'quill'
    allowed_domains = ["quill.com"]
    start_urls = [
        'https://www.quill.com/search?keywords=Gel+Pens',
        'https://www.quill.com/labels/cbl/345.html?filter=Label+Type_Address',
        'https://www.quill.com/search?keywords=Post+it',
        'https://www.quill.com/laminating-machine-and-supplies/cbd/501.html',
        'https://www.quill.com/pens/cbl/598.html?filter=Pen+Type_Ballpoint',
        'https://www.quill.com/dry-erase-makers/cbk/114047.html',
        'https://www.quill.com/permanent-markers/cbk/118131.html',
        'https://www.quill.com/all-purpose-cleaners-degreasers/cbl/4174.html',
        'https://www.quill.com/search?keywords=Cleaning+Wipes',
        'https://www.quill.com/packing-tape/cbl/18190.html'
    ]

    def __init__(self):
        super(QuillSpider, self).__init__()
        pass

    def parse(self, response):
        items = response.css('div#ResultsSection div.BrowseItem')
        for item in items:
            loader = ItemLoader(item=QuillItem(), selector=item)
            loader.add_css('title', 'h3#skuName a::text')
            loader.add_css('price', 'span#SkuPriceUpdate::text')
            loader.add_css('number', 'div#ItemSrchCompare div.iNumber::text')

            yield loader.load_item()

        next_page_data_url = response.css('div#Pager span.next::attr(data-url)').get()
        next_page_query_string = response.css('div#Pager span.next::attr(data-querystring)').get()
        next_page = None
        if next_page_data_url is not None and next_page_query_string is not None:
            next_page = next_page_data_url + '?' + next_page_query_string

        if next_page is not None:
            next_page = response.urljoin(next_page)
            self.logger.info('Next Page : {}'.format(next_page))
            yield scrapy.Request(next_page, callback=self.parse)



