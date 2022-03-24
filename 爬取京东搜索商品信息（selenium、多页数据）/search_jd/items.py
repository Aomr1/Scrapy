# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchJdItem(scrapy.Item):
    title = scrapy.Field()#标题
    price = scrapy.Field()#价格
    commit = scrapy.Field()#评论数
    shop = scrapy.Field()#来源
