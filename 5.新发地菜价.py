import requests
import threading
import math


class Thr(threading.Thread):
    def __init__(self, name, url, headers, data, arr):
        threading.Thread.__init__(self, name=name)
        self.url = url
        self.headers = headers
        self.data = data
        self.arr = arr
        self.count = None

    def run(self):
        req = requests.post(url=self.url, headers=self.headers, data=self.data)
        req.close()
        req = req.json()
        if self.data["current"] == "1":
            self.count = math.ceil(int(req["count"]) / int(self.data["limit"]))
        for item in req["list"]:
            self.arr[item["prodName"]] = [item["avgPrice"], item["prodCat"], item["unitInfo"]]


class Main:
    def __init__(self):
        self.url = "http://www.xinfadi.com.cn/getPriceData.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
        }
        self.data = {
            "current": "1",
            "limit": "100"
        }
        self.arr = {}

    def run(self):
        thr = Thr("thr", self.url, self.headers, self.data, self.arr)
        thr.start()
        thr.join()
        count = thr.count
        for item in range(2, count + 1):
            self.data["current"] = str(item)
            thr = Thr("thr", self.url, self.headers, self.data, self.arr)
            thr.start()
            thr.join()
            while True:
                print("线程：", len(threading.enumerate()), "   ", "数据：", len(self.arr))
                if len(threading.enumerate()) <= 10:
                    break
        while True:
            if len(threading.enumerate()) == 1:
                self.writ()
                break

    def writ(self):
        with open('xfdcj.csv', 'w', encoding="utf-8") as f:
            for k, v in self.arr.items():
                f.write(str(k))
                f.write(",")
                for i in v:
                    f.write(str(i))
                    f.write(",")
                f.write("\n")


if __name__ == '__main__':
    main = Main()
    main.run()
