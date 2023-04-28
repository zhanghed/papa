import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["tupianzj.com"]
    start_urls = ["https://www.tupianzj.com/bizhi/DNqiche/"]

    def parse(self, response):
        print(response.text)
        res = response.xpath('//*[@class="list_con_box_ul"]/li')
        print(res)
        for i in res:
            a = i.xpath('./a/img/@src').extract_first()
            print(a)
