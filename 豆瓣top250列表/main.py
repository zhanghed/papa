import requests, re


# 主对象
class Main:
    def __init__(self):
        self.url = "https://movie.douban.com/top250"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
        }
        self.data = {
            "start": "",
        }

    # 爬取数据
    def req(self):
        for item in range(10):
            self.data["start"] = str(item*25)
            req = requests.get(url=self.url, headers=self.headers, params=self.data)
            req.close()
            rr = re.compile(
                r'<div class="hd">.*?<a href="(?P<url>.*?)" class="">.*?<span class="title">(?P<title>.*?)</span>',
                re.S)
            for i in rr.finditer(req.text):
                Arr[i.group("title")] = [i.group("url")]

    # 写入文件
    def with_to(self):
        with open('top250.csv', 'w', encoding="utf-8") as f:
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
