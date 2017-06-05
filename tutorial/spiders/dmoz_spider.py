# coding=utf-8
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = 'dmoz'  # 对每个spider 名字是唯一的
    allowed_domains = ["http://dmoztools.net"]
    # 为每个start_urls创建scrapy.Request对象，并将parse方法作为回调函数赋给request
    # 经过调度，执行生成scrapy.http.Response对象并送回给parse方法
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/",
    ]

    # 被调用时 每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数
    # 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    def parse(self,response):
        for sel in response.xpath('//div[@class="site-item "]'):
            item = DmozItem()
            item['title'] = sel.xpath('div[3]/a/div/text()').extract()
            item['link'] = sel.xpath('div[3]/a/@href').extract()
            item['desc'] = sel.xpath('div[3]/div/text()').extract()
            yield item
