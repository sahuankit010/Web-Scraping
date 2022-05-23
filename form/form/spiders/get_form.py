import scrapy

def generate_start_urls():
    names = ['Ankit', 'Sarang', 'Rohin']
    quests = ['to ask about rent', 'searching new job profile',
    'sirf bakchodi']
    return ['http://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color=red'.
    format(name,quest) for name in names for quest in quests]

class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['pythonscraping.com']
    start_urls = generate_start_urls()

    def parse(self, response):
        return {
            'text': response.xpath('//div[@class = "wrapper"]/text()').get()
        }
