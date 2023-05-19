import scrapy
from scrapy_selenium import SeleniumRequest
import time
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    name = 'example'
    allowe_domains = ['plumbingsales.com.au']
    sitemap_urls = ['https://plumbingsales.com.au/sitemap.xml']
    
    sitemap_rules = [
        (r'^(.*\/){4,}.*$|^(.*-){5,}.*$', 'start_requests'),
    ]

    def start_requests(self):
        for url in self.sitemap_urls:
            yield SeleniumRequest(url=url, callback=self.parse,wait_time=10)

    def parse(self, response):
        time.sleep(10)
        # print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n----->',response.title)
        yield{
            'url': str(response.url),
        }
