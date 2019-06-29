# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from love.items import LoveItem
class LoveSpiderSpider(CrawlSpider):
    name = 'love_spider'
    allowed_domains = ['yiren98.com']
    start_urls = ['http://www.yiren98.com/se/chengrenkatong/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.yiren98.com/se/chengrenkatong/.+'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        name = response.xpath("//div[@class='mainArea']//font//text()").get()
        srcs = response.xpath("//div[@class='novelContent']//td//img/@src").getall()
        yield LoveItem(name=name, image_urls=srcs)
