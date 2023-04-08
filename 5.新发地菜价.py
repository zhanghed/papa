import requests
import threading
import math
import queue
import datetime
import time


class ThrPro(threading.Thread):
    def __init__(self, name, url, headers, data, que):
        threading.Thread.__init__(self, name=name)
        self.url = url
        self.headers = headers
        self.data = data
        self.arr = []
        self.que = que

    def run(self):
        req = requests.post(url=self.url, headers=self.headers, data=self.data)
        req.close()
        req = req.json()
        for item in req["list"]:
            self.arr.append((item["prodName"], item["avgPrice"], item["prodCat"], item["unitInfo"]))
        self.que.put(self.arr)


class ThrCon(threading.Thread):
    def __init__(self, name, que, event):
        threading.Thread.__init__(self, name=name)
        self.que = que
        self.event = event
        self.arr = []

    def run(self):
        while True:
            if not self.que.empty():
                item = self.que.get_nowait()
                self.arr = self.arr + item
                print(len(self.arr))
            elif self.event.is_set():
                break


class Main:
    def __init__(self):
        self.url = "http://www.xinfadi.com.cn/getPriceData.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
        }
        self.data = {
            "current": "",
            "limit": "20",
            "pubDateStartTime": "",
            "pubDateEndTime": ""
        }
        self.arr = set()
        self.que = queue.Queue()
        self.event = threading.Event()

    def run(self):
        dt = datetime.datetime.today().date()
        self.data["pubDateStartTime"] = str(dt)
        self.data["pubDateEndTime"] = str(dt)
        self.data["current"] = str(1)
        self.data["limit"] = str(20)
        req = requests.post(url=self.url, headers=self.headers, data=self.data)
        req.close()
        req = req.json()
        count = math.ceil(int(req["count"]) / int(self.data["limit"]))
        thr_con = ThrCon("thr_con", self.que, self.event)
        thr_con.start()
        for item in range(1, count + 1):
            self.data["current"] = str(item)
            thr_pro = ThrPro("thr_pro", self.url, self.headers, self.data, self.que)
            thr_pro.start()
            while True:
                time.sleep(0.1)
                if len(threading.enumerate()) < 50:
                    break
        while True:
            ths = threading.enumerate()
            if len(ths) == 2 and self.que.empty() and (ths[0].name == "thr_con" or ths[1].name == "thr_con"):
                self.event.set()
                self.arr = thr_con.arr
                self.writ()
                break

    def writ(self):
        with open('xfdcj.csv', 'w', encoding="utf-8") as f:
            for item in self.arr:
                for i in item:
                    f.write(str(i))
                    f.write(",")
                f.write("\n")


if __name__ == '__main__':
    main = Main()
    main.run()
