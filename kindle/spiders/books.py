import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://www.gutenberg.org/ebooks/bookshelf/68']

    def parse(self, response):
        yield from response.follow_all(css='.booklink > a ::attr(href)', callback=self.parse_book)
    
    def parse_book(self, response):
        links = response.xpath('//a[contains(text(),"Kindle")]/@href').getall()
        for link in links:
            item= {
                'Title' : response.css('h1 ::text').get(),
                'file_urls': [response.urljoin(link)]
                }
            yield item
