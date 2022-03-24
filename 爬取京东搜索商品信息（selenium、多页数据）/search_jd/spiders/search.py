from scrapy import Request
from scrapy.spiders import Spider
from search_jd.items import SearchJdItem#导入Item模块
from selenium import webdriver#导入浏览器引擎模块
import time
import re

class SearchSpider(Spider):
    name = 'search'
    current_page = 1
    total_page = 0
    keyword = 'iphone'
    
    def __init__(self):
    #创建Chrome的对象driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=r'.\spiders\chromedriver.exe',
                          options=chrome_options)
        
    def closed(self,reason):
        self.driver.close()
        
    def start_requests(self):
        url = 'https://search.jd.com/Search?keyword={}&page=1'.format(self.keyword)
        #生成请求对象，设置url
        yield Request(url)

    def parse(self, response):
        records = response.xpath(r'//div[@class="gl-i-wrap"]')
        for record in records:
            try:
                title = ''.join(record.xpath('.//div[@class="p-name p-name-type-2"]/a/em//text()').extract()).strip()
                price = record.xpath('.//div[@class="p-price"]//strong//i/text()').extract_first().strip()
                commit = record.xpath('.//div[@class="p-commit"]/strong/a//text()').extract_first().strip()
                shop = record.xpath('.//div[@class="p-shop"]//span//text()').extract_first().strip()
                item = SearchJdItem()
                re_title = re.findall(r'[^\t\n]+',title)
                item['title'] = ''.join(re_title)
                item['price'] = price
                item['commit'] = commit
                item['shop'] = shop
                yield item
            except:
                print("error")
                pass
            
        if self.current_page == 1:
            self.total_page = int(response.xpath(r'//*[@id="J_bottomPage"]/span[2]/em[1]/b/text()').extract_first())
        
        self.current_page += 2
        
        if self.current_page <= self.total_page*2 + 1:
            next_url = 'https://search.jd.com/Search?keyword={}&page={}'.format(self.keyword,self.current_page)
            yield Request(next_url, callback = self.parse)