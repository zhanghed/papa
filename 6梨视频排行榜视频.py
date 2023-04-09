import requests
import re
import threading
from lxml import etree


class Thr(threading.Thread):
    def __init__(self, name, item):
        threading.Thread.__init__(self, name=name)
        self.item = item

    def run(self):
        url = "https://www.pearvideo.com/videoStatus.jsp"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
            "Content-Type": "application/json;charset=utf-8",
            "Referer": "https://www.pearvideo.com/" + self.item["href"]
        }
        data = {
            "contId": int(re.findall("video_(.*)", self.item["href"])[0])
        }
        req = requests.get(url=url, headers=headers, params=data)
        req.close()
        req = req.json()
        a = req["videoInfo"]["video_image"]
        b = req["videoInfo"]["videos"]["srcUrl"]

        url = re.findall("https.*/", b)[0] + re.findall("cont-.*-", a)[0] + re.findall("-(.*)", b)[
            0]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
            "Content-Type": "application/json;charset=utf-8",
        }
        req = requests.get(url=url, headers=headers)
        req.close()
        self.item["req"] = req.content

        with open(self.item["href"] + '.mp4', "wb") as f:
            f.write(self.item["req"])


class Main:
    def __init__(self):
        self.arr = []

    def run(self):
        url = "https://www.pearvideo.com/popular"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
            "Content-Type": "application/json;charset=utf-8"
        }
        req = requests.get(url=url, headers=headers)
        req.close()
        req = etree.HTML(req.text)
        req = req.xpath(r'//*[@id="popularList"]/li')
        for item in req:
            item = etree.tostring(item, encoding='utf-8').decode()
            rr = re.compile(
                '<div class="popularem-ath">.*?<a href="(?P<href>.*?)" class="popularembd actplay">', re.S)
            for i in rr.finditer(item):
                self.arr.append({"href": i.group(("href"))})
        for item in self.arr:
            thr = Thr("thr", item)
            thr.start()


if __name__ == '__main__':
    main = Main()
    main.run()
    while True:
        ths = threading.enumerate()
        print(len(ths))
        if len(ths) == 1:
            print("end")
            break
