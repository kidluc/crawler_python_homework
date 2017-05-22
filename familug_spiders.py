import scrapy
from scrapy.selector import Selector


class FamilugSpider(scrapy.Spider):
    name = 'Familug'

    start_urls = ['http://familug.org/']

    def parse(self, response):
        # selector HTML CODE
        hxs = Selector(response)
        info = hxs.xpath('//div[@class="post-outer"]')

        # Loop info
        for item in info:
            title = item.xpath('//h3[@class="post-title entry-title"]'
                               '/a/text()').extract()
            link = item.xpath('//h3[@class="post-title entry-title"]/'
                              'a/@href').extract()
            author = item.xpath('//span[@itemprop="name"]/text()').extract()
            info_page = (list(zip(title, link, author)))
        # write to file
        with open('fml.json', 'w+') as f:
            f.write(str(info_page))

        '''
        # calling next page
        next_page = response.css('//div.blog-pager
        a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        '''
