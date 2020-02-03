import os
import scrapy
from selenium import webdriver
from scrapy.selector import Selector

basedir = os.path.dirname(os.path.realpath('__file__'))


class InvestingSpider(scrapy.Spider):
    name = 'investing'
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')

        web_driver_path = os.path.join(basedir, 'chromedriver')
        driver = webdriver.Chrome(web_driver_path, chrome_options=options)
        driver.get('https://www.investing.com/analysis/forex')

        detail_urls = []
        scrapy_selector = Selector(text=driver.page_source)
        article_elements = scrapy_selector.xpath('//*[@id="contentSection"]/article')
        for element in article_elements:
            url_portion = element.css('div.textDiv > a.title::attr(href)').get()
            if url_portion is not None:
                detail_url = 'https://www.investing.com' + url_portion
                detail_urls.append(detail_url)

        for detail_url in detail_urls:
            driver.get(detail_url)
            scrapy_selector = Selector(text=driver.page_source)
            title = scrapy_selector.css('#leftColumn > h1.articleHeader::text').get()

            text_elements = scrapy_selector.css('div#articlePage > div.articlePage > p')
            content = ''
            for text_element in text_elements:
                content += text_element.xpath('string()').get()

            yield {
                'title': title,
                'content': content
            }

        driver.close()

