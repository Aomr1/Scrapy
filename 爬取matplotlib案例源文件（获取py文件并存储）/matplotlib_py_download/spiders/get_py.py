from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from matplotlib_py_download.items import MatplotlibPyDownloadItem#导入Item

class GetPySpider(Spider):
    name = 'get_py'
    
    def start_requests(self):
        url = 'https://matplotlib.org/stable/gallery/index'
        yield Request(url)
        
    def parse(self, response):
        urls = response.xpath('//div[@class="sphx-glr-thumbcontainer"]//a[@class="reference internal"]/@href').extract()
        for i in range(len(urls)):
            url = response.urljoin(urls[i])
            print('当前下载量：',str(int(i)+1))
            yield Request(url,callback = self.parse_file)
    
    def parse_file(self,response):
        href = response.xpath('//div[@class="sphx-glr-download sphx-glr-download-python docutils container"]/p/a/@href').extract_first()
        py_url = response.urljoin(href)
        item = MatplotlibPyDownloadItem()
        item['file_urls'] = [py_url]
        
        yield item
        
        
        