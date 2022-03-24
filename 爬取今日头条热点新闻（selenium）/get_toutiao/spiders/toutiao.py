from scrapy import Request
from scrapy.spiders import Spider
from get_toutiao.items import GetToutiaoItem#导入Item模块
from selenium import webdriver#导入浏览器引擎模块
import re
class ToutiaoSpider(Spider):
    #定义爬虫名称
    name = 'toutiao'
    def __init__(self):
    #创建Chrome的对象driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=r'.\spiders\chromedriver.exe',
                          options=chrome_options)
    def closed(self,reason):
        self.driver.close()
    #获取初始Request
    def start_requests(self):
        url = 'https://www.toutiao.com/?channel=hot&source=ch'
        #生成请求对象，设置url
        yield Request(url)
    # 数据解析
    def parse(self, response):
        item = GetToutiaoItem()
        list_selector = response.xpath('//div[@class="feed-card-article-l"]')
        for selector in list_selector:
            try:
                #标题
                title = selector.xpath('.//h2/text()').extract_first()
                #来源
                source = selector.xpath('.//div[@class="feed-card-footer-cmp-author"]/a/text()').extract_first()
                #评论数
                comment = selector.xpath('.//div[@class="feed-card-footer-comment-cmp"]/a/text()').extract_first()
                item["title"] = title#标题
                item["source"] = source#来源
                item["comment"] = re.findall(r'[0-9]+', comment)[0]#评论数
                yield item
            except:
                continue