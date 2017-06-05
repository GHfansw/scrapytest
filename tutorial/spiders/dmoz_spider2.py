# coding=utf-8
import scrapy
from tutorial.items import DmozItem
from tutorial.items import RZItem


class DmozSpider(scrapy.Spider):
    name = 'rz'  # 对每个spider 名字是唯一的
    allowed_domains = ["http://djangobook.py3k.cn"]
    start_urls = [
       "http://djangobook.py3k.cn/2.0/",
    ]

    def parse(self,response):
        for href in response.css("li.a > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse2)

    def parse2(self,response):
        self.logger.info("Visited %s", response.url)
