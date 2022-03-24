# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MatplotlibPyDownloadItem(scrapy.Item):
    file_urls = scrapy.Field()#文件url地址
    files = scrapy.Field()#文件下载信息
