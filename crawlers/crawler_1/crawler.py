import scrapy

class Crawler1Spider(scrapy.Spider):
    name = "crawler_1"
    start_urls = ['http://example.com']

    def parse(self, response):
        yield {"url": response.url, "title": response.css("title::text").get()}