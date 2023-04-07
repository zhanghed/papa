import requests
import re
from lxml import etree


# 主对象
class Main:
    def __init__(self):
        self.url = "https://beijing.zbj.com/search/service/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
        }
        self.data = {
            "fr": "header",
            "kw": "小程序开发",
            "l": "0",
            "r": "2",

        }

    # 爬取数据
    def req(self):
        req = requests.get(url=self.url, headers=self.headers, params=self.data)
        req.close()
        req = etree.HTML(req.text)
        req = req.xpath(r'//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]')[0]
        req = req.xpath(r'./div')
        for item in req:
            item = etree.tostring(item, encoding='utf-8').decode()
            rr = re.compile(
                '<div class="shop-info text-overflow-line">(?P<title>.*?)</div>.*?<div class="price">.*?<span>(?P<price>.*?)</span>.*?class="serve-name.*?>(?P<name>.*?)</a>',
                re.S)
            for i in rr.finditer(item):
                Arr[i.group(("title"))] = [i.group(("name")), i.group(("price"))]

    # 写入文件
    def with_to(self):
        with open('zbjxcx.csv', 'w', encoding="utf-8") as f:
            for k, v in Arr.items():
                f.write(str(k))
                f.write(",")
                for i in v:
                    f.write(str(i))
                    f.write(",")
                f.write("\n")


if __name__ == '__main__':
    Arr = {}
    main = Main()
    main.req()
    main.with_to()
