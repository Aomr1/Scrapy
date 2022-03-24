# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WallpapersJpgDownloadItem(scrapy.Item):
    title = scrapy.Field()#图片名称
    image_urls = scrapy.Field()#图片URL地址
    images = scrapy.Field()    #图片下载信息
