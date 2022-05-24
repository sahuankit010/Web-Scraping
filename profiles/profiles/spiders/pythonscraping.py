import scrapy


class PythonscrapingSpider(scrapy.Spider):
    name = 'pythonscraping'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/']

    def parse(self, response):
        pass
