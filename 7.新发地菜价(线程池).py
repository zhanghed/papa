import requests
import threading
import queue
import datetime
import math
from timeit import default_timer
from concurrent.futures import ThreadPoolExecutor, as_completed


class Main:
    def __init__(self):
        self.url = "http://www.xinfadi.com.cn/getPriceData.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
        }
        dt = str(datetime.datetime.today().date())
        self.data = {"current": "1", "limit": "20", "pubDateStartTime": dt, "pubDateEndTime": dt}
        self.count = 0
        self.arr = []
        self.que = queue.Queue()
        self.event = threading.Event()

    def run(self):
        self.req_one()
        with ThreadPoolExecutor(max_workers=10) as t:
            t.submit(self.req_c)
            n = range(1, self.count + 1)
            s = [t.submit(self.req_p, str(i)) for i in n]
            for _ in as_completed(s):
                pass
            self.event.set()
            self.write()

    def req_one(self):
        req = requests.post(url=self.url, headers=self.headers, data=self.data)
        req.close()
        req = req.json()
        self.count = math.ceil(int(req["count"]) / int(self.data["limit"]))

    def req_p(self, c):
        self.data["current"] = c
        req = requests.post(url=self.url, headers=self.headers, data=self.data)
        req.close()
        req = req.json()
        temp = []
        for item in req["list"]:
            temp.append((item["prodName"], item["avgPrice"], item["prodCat"], item["unitInfo"]))
        self.que.put(temp)
        print(len(temp),threading.enumerate())

    def req_c(self):
        while True:
            if not self.que.empty():
                self.arr.append(self.que.get_nowait())
            elif self.event.is_set():
                break

    def write(self):
        with open("aaaaa" + '.csv', "w", encoding="utf-8") as f:
            for item in self.arr:
                for i in item:
                    for ii in i:
                        f.write(ii)
                        f.write(",")
                    f.write("\n")


if __name__ == '__main__':
    a = default_timer()
    main = Main()
    main.run()
    b = default_timer()
    print(b - a)
