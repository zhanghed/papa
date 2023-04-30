import scrapy
from douban250.items import Douban250Item


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250?start=%s&filter="]

    def start_requests(self):
        for i in range(10):
            yield scrapy.Request(
                url=self.start_urls[0] % (str(i*25)),
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/111.0.0.0 Safari/537.36",
                },
                callback=self.parse
            )

    def parse(self, response):
        res = response.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li')
        for i in res:
            data = Douban250Item()
            data["name"] = i.xpath('.//span[@class="title"]/text()').get()
            data["url"] = i.xpath('.//a[@class=""]/@href').get()
            yield data
