import scrapy
from scrapy.http import *


class GetFormSpider(scrapy.Spider):
    name = 'post_form'
    allowed_domains = ['pythonscraping.com']

    def start_requests(self):
        names = ['Ankit', 'Sarang', 'Rohin']
        quests = ['to ask about rent', 'searching new job profile',
        'sirf bakchodi']
        colors= ['red', 'blue', 'cyan']
        return [FormRequest('http://pythonscraping.com/linkedin/formAction2.php',
        formdata = {'name': name, 'quest': quest, 'color': color},
        callback = self.parse) for name in names for quest in quests for color in colors]

    def parse(self, response):
        return {
            'text': response.xpath('//div[@class = "wrapper"]/text()').get()
        }
