# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()  #书名
    author = scrapy.Field()  #作者
    book_info =scrapy.Field() #书籍信息
    grade = scrapy.Field()      #评分
    quote =scrapy.Field()       #短语
    img_url = scrapy.Field()    #封面地址
    rank = scrapy.Field()   #排名


    pass
