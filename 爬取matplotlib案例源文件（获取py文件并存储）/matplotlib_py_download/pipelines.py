# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from scrapy.pipelines.files import FilesPipeline#导入文件管道类

class MatplotlibPyDownloadPipeline:
    def process_item(self, item, spider):
        return item


#定义新的文件管道，继承于FilesPipeline
class SaveFilePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        #获取文件名，并返回
        return request.url.split("/")[-1]