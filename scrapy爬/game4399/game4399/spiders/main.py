import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["4399.com"]
    start_urls = ["https://www.4399.com/flash/"]

    def parse(self, response):
        r = response.xpath("/html/body/div[8]/ul/li")
        for i in r:
            a = i.xpath("./a/@href").extract_first()
            b = i.xpath("./a/b/text()").extract_first()
            data = {
                "name": b,
                "url": a
            }
            print(data)
