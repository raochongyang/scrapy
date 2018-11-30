import scrapy
from tutorial.items import NovelItem
class NovelSpider(scrapy.Spider):
    name = "novel"
    allowed_domains= ["readnovel.com"]
    start_urls = [

        "https://www.readnovel.com/"
    ]
    def parse(self, response):
        item = NovelItem()
        for sel in response.xpath("//*[@id='new-book-list']/div/ul/li/div[2]"):
            item['title'] = sel.xpath("//*[@id='new-book-list']/div/ul/li/div[2]/h4/a/text()").extract()
            item['link'] = sel.xpath("//*[@id='new-book-list']/div/ul/li/div[2]/h4/a/@href").extract()
            item['author'] = sel.xpath("//*[@id='new-book-list']/div/ul/li/div[2]/div/a/text()").extract()
            item['type'] = sel.xpath("//*[@id='new-book-list']/div/ul/li/div[2]/div/i/text()").extract()
        yield item

