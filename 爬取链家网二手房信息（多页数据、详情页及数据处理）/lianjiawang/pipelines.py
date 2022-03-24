# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import re
from scrapy.exceptions import DropItem

class FilterPipeline(object):
    def process_item(self, item, spider):
        item["area"] = re.findall(r"\d+\.?\d*",item["area"])[0]
        item["unit_price"] = ''.join(re.findall(r"\d+\,?\d*",item["unit_price"])[0].split(","))
        if item["direction"] == "暂无数据":
            raise DropItem("房屋朝向无数据，抛弃此项目: %s"%item)
        elif item["property"] == "暂无数据":
            raise DropItem("电梯一栏无数据，抛弃此项目: %s"%item)
        return item

class CSVPipeline(object):
    index = 0
    file = None
    
    def open_spider(self,spider):
        self.file = open("lianjia_data.csv","a",encoding="gb18030")

    def process_item(self, item, spider):
        if self.index == 0:
            column_name = "房屋名称,房屋户型,建筑面积,房屋朝向,装修情况,有无电梯,房屋总价,房屋单价,\n"
            self.file.write(column_name)
            self.index = 1

        home_str =  item['name']+","+\
                    item["type"]+","+\
                    item["area"]+","+ \
                    item["direction"] + "," + \
                    item["fitment"] + "," + \
                    item["property"] + "," + \
                    item["total_price"] + "," + \
                    item["unit_price"] + "\n"

        self.file.write(home_str)
        return item


    def close_spider(self,spider):
        self.file.close()
