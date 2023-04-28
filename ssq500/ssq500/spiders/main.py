import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["datachart.500.com"]
    start_urls = ["https://datachart.500.com/ssq/"]

    def parse(self, response):
        res = response.xpath('//*[@id="tdata"]/tr')
        for i in res:
            a = i.xpath('./td[@align="center"]/text()').extract_first()
            b = i.xpath('./td[@class="chartBall01"]/text()').extract()
            c = i.xpath('./td[@class="chartBall02"]/text()').extract_first()
            temp = {
                "center": a,
                "chartball01": b,
                "chartball02": c,
            }
            yield temp
