# -*- coding: utf-8 -*-
import scrapy


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['https://www.douban.com/']
    start_urls = ['http://https://www.douban.com//']

    def parse(self, response):
        pass
