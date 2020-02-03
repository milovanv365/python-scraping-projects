from davescraper.spiders.quill_spider import QuillSpider
from davescraper.spiders.investing_spider import InvestingSpider
from scrapy.crawler import CrawlerProcess
import os

basedir = os.path.dirname(os.path.realpath('__file__'))
output_dir = basedir + '/output/'


def main():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': output_dir + '%(name)s_111.json'
    })

    # process.crawl(QuillSpider)
    process.crawl(InvestingSpider)
    process.start()


if __name__ == '__main__':
    main()
