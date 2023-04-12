import asyncio
import datetime
import math
import threading
from timeit import default_timer

import aiofiles
import aiohttp
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

    async def run(self):
        req = requests.post(url=self.url, headers=self.headers, data=self.data)
        req.close()
        req = req.json()
        self.count = math.ceil(int(req["count"]) / int(self.data["limit"]))

        tasks = []
        for item in range(1, self.count + 1):
            self.data["current"] = str(item)
            t = self.download()
            task = asyncio.create_task(t)
            tasks.append(task)
        await asyncio.wait(tasks)

    async def download(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(url=self.url, headers=self.headers, data=self.data) as req:
                req = await req.json()
                temp = []
                for item in req["list"]:
                    temp.append((item["prodName"], item["avgPrice"], item["prodCat"], item["unitInfo"]))
                async with aiofiles.open("./temp/" + self.data["current"] + '.csv', "w", encoding="utf-8") as f:
                    for item in temp:
                        for i in item:
                            await f.write(i)
                            await f.write(",")
                        await f.write("\n")
                print(len(temp), len(threading.enumerate()))


if __name__ == '__main__':
    a = default_timer()

    main = Main()
    asyncio.run(main.run())
    print(len(threading.enumerate()))

    b = default_timer()
    print(b - a)
