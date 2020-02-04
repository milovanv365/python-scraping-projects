from davescraper.spiders.quill_spider import QuillSpider
from davescraper.spiders.investing_spider import InvestingSpider
from scrapy.crawler import CrawlerProcess


def main():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output/%(name)s.json'
    })

    while True:
        target_site = input("Enter Target Site(investing/quill):").lower()
        if target_site == 'investing' or target_site == 'quill':
            break

    if target_site == 'investing':
        process.crawl(InvestingSpider)
    elif target_site == 'quill':
        process.crawl(QuillSpider)
    else:
        pass

    process.start()


if __name__ == '__main__':
    main()
