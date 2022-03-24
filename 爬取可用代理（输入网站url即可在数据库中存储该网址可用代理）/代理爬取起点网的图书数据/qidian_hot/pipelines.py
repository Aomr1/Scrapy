# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class QidianHotPipeline(object):
    def process_item(self, item, spider):
        #判断小说形式是连载还是完结
        if item["form"] == "连载":#连载的情况
            item["form"] = "LZ"#替换为简称
        else:#其他情况
            item["form"] = "WJ"
        return item

#去除重复作者的Item Pipeline
class DuplicatesPipeline(object):
    def __init__(self):
        #定义一个保存作者姓名的集合，
        self.author_set = set()
    def process_item(self, item, spider):
        if item['author'] in self.author_set:
            #抛弃重复的Item项
            raise DropItem("查找到重复姓名的项目: %s"%item)
        else:
            self.author_set.add(item['author'])
        return item