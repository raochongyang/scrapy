# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from scrapy.http import Request



from scrapy.exporters import JsonItemExporter
class JsonExporterPipeline:
    # 调用 scrapy 提供的 json exporter 导出 json 文件
    def __init__(self):
        self.file = open('questions_exporter.json', 'wb')
        # 初始化 exporter 实例，执行输出的文件和编码
        self.exporter = JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        # 开启倒数
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class DoubanbookSpider(scrapy.Spider):
    name = 'doubanbook'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/top250']

    def start_requests(self):
        pages = []
        for i in range(0, 10):
            url = 'https://book.douban.com/top250/?start=%s' % (i*25)
            page = scrapy.Request(url)
            pages.append(page)
        return pages



    def parse(self, response):
        item = DoubanItem()
        writers = []
        rank = []
        titles = response.xpath("//*[@id='content']/div/div[1]/div[1]/table/tr/td[2]/div[1]/a/@title").extract()
        bookinfos = response.xpath("//*[@id='content']/div/div[1]/div[1]/table/tr/td[2]/p[1]/text()").extract()
        grades = response.xpath("//*[@id='content']/div/div[1]/div[1]/table/tr/td[2]/div[2]/span[2]/text()").extract()
        quotes = response.xpath("//*[@id='content']/div/div[1]/div[1]/table/tr/td[2]/p[2]/span/text()").extract()
        img_urls = response.xpath("//*[@id='content']/div/div/div/table/tr/td/a/img/@src").extract()
        ranks = response.xpath("//*[@id='content']/div/div[1]/div[1]/table/tr/td/a/@onclick").extract()
        for author in bookinfos:
            writers.append(author.split("/")[0])

        item['author'] = writers
        item['title'] = titles
        item['grade'] = grades
        item['quote'] = quotes
        item['img_url'] = img_urls
        item['book_info'] = bookinfos

        yield item











