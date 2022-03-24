import scrapy
from lianjiawang.items import LianjiawangItem

class LianjiaScrapyDemoSpider(scrapy.Spider):
    name = 'lianjia_scrapy_demo'
    current_page = 1
    total_page = 0
    
    def start_requests(self):
        url = 'https://su.lianjia.com/ershoufang/'
        yield scrapy.Request(url)
    
    def parse(self, response):
        records = response.xpath(r'//li/div[@class="info clear"]')
        for record in records:
            try:
                name = record.xpath(r'./div[@class="flood"]//a/text()').extract_first().strip()
                other = record.xpath(r'./div[@class="address"]//text()').extract_first()
                other_list = other.split('|')
                type = other_list[0].strip()
                area = other_list[1].strip()
                direction = other_list[2].strip()
                fitment = other_list[3].strip()
                price_list = record.xpath('./div[@class="priceInfo"]//span/text()').extract()
                total_price = price_list[0]
                unit_price = price_list[1]
                
                item = LianjiawangItem()
                item['name'] = name
                item['type'] = type
                item['area'] = area
                item['direction'] = direction
                item['fitment'] = fitment
                item['total_price'] = total_price
                item['unit_price'] = unit_price
                
                detail_url = record.xpath('./div[@class="title"]/a/@href').extract_first()
                yield scrapy.Request(detail_url, meta = {'item':item}, callback = self.detail_parse)
            except:
                print("error")
                pass
            
        if self.current_page == 1:
            self.total_page = int(response.xpath(r'//div[@class="page-box house-lst-page-box"]//@page-data')
                                  .re(r'[0-9]+')[0])
        
        self.current_page += 1
        
        if self.current_page <= 10:#self.total_page
            next_url = "https://su.lianjia.com/ershoufang/pg{}".format(self.current_page)
            yield scrapy.Request(next_url, callback = self.parse)
        
    def detail_parse(self,response):
        item = response.meta['item']
        property = response.xpath("//div[@class='base']/div[@class='content']/ul/li[last()]/text()").extract_first()
        item['property'] = property
        yield item
                