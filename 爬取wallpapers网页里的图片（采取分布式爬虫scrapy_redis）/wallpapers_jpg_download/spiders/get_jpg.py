from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from wallpapers_jpg_download.items import WallpapersJpgDownloadItem#导入Item
import re

from scrapy_redis.spiders import RedisSpider#导入RedisSpider

class GetJpgSpider(RedisSpider):
    name = 'get_jpg'
    current_page = 1
    total_page = 0
    
    # def start_requests(self):
    #     url = 'http://wallpaperswide.com/page/1'
    #     yield Request(url)
        
    def parse(self,response):
        urls = response.xpath('//div[@id="hudtitle"]/a/@href').extract()
        for i in range(len(urls)):
            item = WallpapersJpgDownloadItem()
            url = response.urljoin(urls[i])
            title = re.findall(r'http://wallpaperswide.com/(.*)-wallpapers.html',url)[0]
            item['title'] = title
            yield Request(url,meta = {'item':item},callback = self.parse_image)
            
        if self.current_page == 1:
            self.total_page = int(response.xpath(r'//*[@id="content"]/div[3]/a[2]/text()').extract_first())
        
        self.current_page += 1
        
        if self.current_page <= 2:#self.total_page
            next_url = "http://wallpaperswide.com/page/{}".format(self.current_page)
            yield Request(next_url, callback = self.parse)
            
    def parse_image(self,response):
        item = response.meta['item']
        href = response.xpath('//a[@title="HD 16:9 1920 x 1080 wallpaper for FHD 1080p High Definition or Full HD displays"]/@href').extract_first()
        image_url =  response.urljoin(href)
        item["image_urls"] = [image_url]
        yield item

