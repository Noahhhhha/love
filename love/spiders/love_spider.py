# -*- coding: utf-8 -*-
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
        name = response.xpath("//div[@class='mainArea']//font//text()").get() # 每一页的名字
        srcs = response.xpath("//div[@class='novelContent']//td//img/@src").getall() # 每一页所有照片的url
        # print(response.request.headers['User-Agent']) # 测试一下消息头有没有随机成功
        print(response.request.headers['User-Agent'])  # 测试一下消息头有没有随机成功
        yield LoveItem(name=name, image_urls=srcs)
