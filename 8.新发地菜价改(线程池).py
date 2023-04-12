import datetime
import math
import threading
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer

import requests


class Main:
    def __init__(self):
        self.url = "http://www.xinfadi.com.cn/getPriceData.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
        }
        dt = str(datetime.date.today())
        dt = str(datetime.date(year=2023, month=4, day=11))
        self.data = {"current": "1", "limit": "20", "pubDateStartTime": dt, "pubDateEndTime": dt}
        self.count = 0

    def run(self):
        req = requests.post(url=self.url, headers=self.headers, data=self.data)
        req.close()
        req = req.json()
        self.count = math.ceil(int(req["count"]) / int(self.data["limit"]))

        with ThreadPoolExecutor(max_workers=10) as t:
            n = range(1, self.count + 1)
            for item in n:
                t.submit(self.download, str(item))

    def download(self, c):
        self.data["current"] = c
        req = requests.post(url=self.url, headers=self.headers, data=self.data)
        req.close()
        req = req.json()
        temp = [c]
        for item in req["list"]:
            temp.append((item["prodName"], item["avgPrice"], item["prodCat"], item["unitInfo"]))
        with open("./temp/" + c + '.csv', "w", encoding="utf-8") as f:
            for item in temp[1]:
                for i in item:
                    f.write(i)
                    f.write(",")
                f.write("\n")
        print(len(temp), len(threading.enumerate()))


if __name__ == '__main__':
    a = default_timer()

    main = Main()
    main.run()
    print(len(threading.enumerate()))

    b = default_timer()
    print(b - a)
