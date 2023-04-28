import scrapy
from ssq500 import items


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["datachart.500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    def parse(self, response):
        res = response.xpath('//*[@id="tdata"]/tr')
        for i in res:
            a = i.xpath('./td[@align="center"]/text()').extract_first()
            if a == None:
                continue
            b = i.xpath('./td[@class="chartBall01"]/text()').extract()
            c = i.xpath('./td[@class="chartBall02"]/text()').extract_first()

            item = items.Ssq500Item()
            item["center"] = a
            item["chartball01"] = b
            item["chartball02"] = c

            yield item
