# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from scrapy import Request
import re
from scrapy.pipelines.images import ImagesPipeline#导入图片管道类

class WallpapersJpgDownloadPipeline:
    def process_item(self, item, spider):
        return item


#图片管道，继承于ImagesPipeline
class SaveImagePipeline(ImagesPipeline):
    #构造图像下载的请求，url从item["image_urls"]中获取
    # def get_media_requests(self, item, info):
    #     yield Request(item['image_urls'],meta={'title':item['title']})

    #设置图片存储路径及名称
    def file_path(self, request, response=None, info=None):
        image_name = re.findall(r'(.*)-wallpaper-1920x1080',request.url.split("/")[-1])[0]
        #图片存储形式：图片类型/图片名称
        return '{}.jpg'.format(image_name)
    
    # #设置缩略图存储路径及名称
    # def thumb_path(self, request, thumb_id, response=None, info=None):
    #     #从Request中meta中获取图片类型
    #     title = request.meta["title"]
    #     image_name = request.url.split("/")[-1]
    #     #缩略图路径：图片类型名/big(或small)/图片名称
    #     return '%s/%s/%s' % (title,thumb_id,image_name)
    
    # def item_completed(self, results, item, info):
    #     item['images'] = [x for ok, x in results if ok]
    #     return item
