# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiawangItem(scrapy.Item):
    name = scrapy.Field()       #房屋名称
    type = scrapy.Field()       #房屋户型
    area = scrapy.Field()       #建筑面积
    direction = scrapy.Field()  #房屋朝向
    fitment = scrapy.Field()    #装修情况
    elevator = scrapy.Field()   #有无电梯
    total_price = scrapy.Field()#房屋总价
    unit_price = scrapy.Field() #房屋单价
    property = scrapy.Field()   #房屋产权
