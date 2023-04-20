import requests, time


# 主对象
class Main:
    def __init__(self):
        self.url = "https://cn.bing.com/HPImageArchive.aspx"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1111111111; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        }
        self.data = {
            'format': 'js',
            'idx': '1',
            'n': '999',
            'nc': int(round((time.time()) * 1000)),
            'pid': 'hp',
        }

    # 爬取数据
    def req(self):
        req = requests.get(url=self.url, headers=self.headers, params=self.data)
        req.close()
        req = req.json()
        for item in req["images"]:
            title = item['title']
            url = "https://cn.bing.com" + item['url']
            req = requests.get(url=url, headers=self.headers)
            req.close()
            Arr[title] = req.content

    # 写入文件
    def with_to(self):
        for k, v in Arr.items():
            with open(k + '.jpg', 'wb') as f:
                f.write(v)


if __name__ == '__main__':
    Arr = {}
    main = Main()
    main.req()
    main.with_to()
