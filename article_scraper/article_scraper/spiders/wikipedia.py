import scrapy
from scrapy.spiders import *
from scrapy.linkextractors import *


class WikipediaSpider(CrawlSpider):

    name = 'wikipedia'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://wikipedia.org/wiki/Kevin_Bacon']

    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)]

    def parse_info(self, response):
        return {
            'title': response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get(),
            'url': response.url,
            'last_updated': response.xpath('//li[@id = "footer-info-lastmod"]').get(),
        }
