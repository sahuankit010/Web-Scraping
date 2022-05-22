import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):

        #using css
        #title = response.css('span.title::text').get()
        #using xpath
        title = response.xpath('//span[@class = "title"]/text()').get()
        # print(title)
        return {"title": title}
        pass
