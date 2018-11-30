# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import json
from scrapy.exporters import JsonItemExporter
# 去除空的数据
class AddPipeline:
    def process_item(self,items,spider):
        if len(items['quote'])<len(items['title']):
            for i in range(0,(len(items['title'])-len(items['quote']))):
                items['quote'].append("无")
            return items
        else:
            return items


class JsonExporterPipeline:
    # 调用 scrapy 提供的 json exporter 导出 json 文件
    def __init__(self):
        self.file = open('douban.json', 'wb')
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





class DisposePipline(object):
    def __init__(self):
        self.title_list = []
        self.author_list = []
        self.bookinfo_list = []
        self.grade_list = []
        self.quote_list = []
        self.img_url_list =[]
        self.book_list = []
        self.book_dict = {'name': '', 'author': '', 'book_info': '', 'grade': '', 'quote': '', 'img_url': ''}
        self.load_dict = ''

    def process_item(self,item,spider):

        with open("douban.json",encoding='UTF-8') as load_f:

            load_dict = json.load(load_f,strict=False)
            for i in load_dict:
                authors = i.get('author')
                names = i.get('title')
                book_infos = i.get('book_info')
                grades = i.get('grade')
                quotes = i.get('quote')
                img_urls = i.get('img_url')
            # load_dict = json.load(load_f)
            # names = load_dict.get("title")
            # book_infos = load_dict.get('book_info')
            # authors = load_dict.get("author")
            # grades = load_dict.get("grade")
            # quotes = load_dict.get("quote")
            # img_urls = load_dict.get("img_url")

        for name in names:
            self.title_list.append(name)
        for author in authors:
            self.author_list.append(author)
        for book_info in book_infos:
            self.bookinfo_list.append(book_info)
        for grade in grades:
            self.grade_list.append(grade)
        for quote in quotes:
            self.quote_list.append(quote)
        for img_url in img_urls:
            self.img_url_list.append(img_url)


        for i in range(0,len(self.quote_list)):
            self.book_dict['name'] = self.title_list[i]
            self.book_dict['author'] = self.author_list[i]
            self.book_dict['book_info'] = self.bookinfo_list[i]
            self.book_dict["grade"] = self.grade_list[i]
            self.book_dict["quote"] = self.quote_list[i]
            self.book_dict['img_url'] = self.img_url_list[i]



            self.book_list.append(self.book_dict)
            self.book_dict = {'name': '', 'author': '', 'book_info': '', 'grade': '', 'quote': '', 'img_url': ''}

        book_list1 = json.dumps(self.book_list, ensure_ascii=False)
        fo = open("jjj.json", "w", encoding='utf-8')
        fo.write(book_list1)
        fo.close()
        return item



















