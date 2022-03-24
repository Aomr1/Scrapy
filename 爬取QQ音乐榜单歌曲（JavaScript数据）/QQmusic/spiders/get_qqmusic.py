from scrapy import Request
from scrapy.spiders import Spider#导入Spider类
from QQmusic.items import QqmusicItem  #导入Item类
import json

class GetQqmusicSpider(Spider):
    name = 'get_qqmusic'
    def start_requests(self):#获取初始请求
        url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?&topid=4"
        #生成请求对象
        yield Request(url)
    
    def parse(self, response):#数据解析函数
        item = QqmusicItem()#生成QqmusicItem对象
        #获取到json格式的数据
        json_text = response.text
        #使用json.loads解码json数据，返回Python支持的数据类型
        #这里的music_dict是一个字典类型
        music_dict = json.loads(json_text)
        #for循环遍历每首歌曲
        for one_music in music_dict["songlist"]:
            #获取歌曲
            item["song_name"] = one_music["data"]["songname"]
            #获取唱片
            item["album_name"] = one_music["data"]["albumname"]
            #获取歌手
            item["singer_name"] = one_music["data"]["singer"][0]["name"]
            #获取时长
            item["interval"] = one_music["data"]["interval"]

            yield item