import requests, re, threading


# 每页汇总线程
class ThrOne(threading.Thread):
    def __init__(self, name, url, headers):
        threading.Thread.__init__(self, name=name)
        self.url = url
        self.headers = headers

    def run(self):
        req = requests.get(url=self.url, headers=self.headers)
        req.close()
        req.encoding = "gb2312"
        req = req.text
        rr = re.compile('<div class="co_content8"(?P<url_list>.*?)/div>', re.S)
        for item in rr.finditer(req):
            rr = re.compile('<a href="(?P<url>.*?)" class="ulink" title="(?P<title>.*?)">', re.S)
            for i in rr.finditer(item.group("url_list")):
                thr = ThrTwo("Thr_two", "https://www.dy2018.com" + i.group("url"), self.headers)
                thr.start()
                Arr[i.group("title")] = thr.req


# 详情数据线程
class ThrTwo(threading.Thread):
    def __init__(self, name, url, headers):
        threading.Thread.__init__(self, name=name)
        self.url = url
        self.headers = headers
        self.req = []

    def run(self):
        req = requests.get(url=self.url, headers=self.headers)
        req.close()
        req.encoding = "gb2312"
        req = req.text
        rr = re.compile('<div id="downlist"(?P<url_list>.*?)/div>', re.S)
        for i in rr.finditer(req):
            rr = re.compile('<a href="(?P<url>.*?)">', re.S)
            for ii in rr.finditer(i.group("url_list")):
                self.req.append(ii.group("url").replace("\r", ""))


# 主对象
class Main:
    def __init__(self):
        self.url = "https://www.dy2018.com/html/bikan/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
        }
        self.count = self.get_count()
        self.urls = self.get_urls()

    # 获取总页数
    def get_count(self):
        req = requests.get(url=self.url + "index.html", headers=self.headers)
        req.close()
        req.encoding = "gb2312"
        req = req.text
        rr = re.compile('页次：.*?/(?P<count>.*?)&nbsp;每页', re.S)
        for item in rr.finditer(req):
            return int(item.group("count"))

    # 生成每页连接
    def get_urls(self):
        urls = ["https://www.dy2018.com/html/bikan/index.html"]
        for item in range(1, self.count + 1):
            urls.append("https://www.dy2018.com/html/bikan/index_" + str(item) + ".html")
        return urls

    # 爬取数据
    def req(self):
        for url in self.urls:
            thr = ThrOne("Thr_one", url, self.headers)
            thr.start()

    # 写入文件
    def with_to(self):
        with open('dianyingtiantang_urls.csv', 'w', encoding="utf-8") as f:
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

    # 主线程
    while True:
        print("线程：", len(threading.enumerate()), "      ", "数据：", len(Arr))
        if len(threading.enumerate()) == 1:
            main.with_to()
            break
