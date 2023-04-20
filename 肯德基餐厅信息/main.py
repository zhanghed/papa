import asyncio
import base64
import json
from timeit import default_timer

import aiofiles
import aiohttp
import requests
from Crypto.Cipher import AES
from lxml import etree
import math


class Main:
    def __init__(self):
        self.arr = []
        self.count = None

    async def run(self):
        await self.init()
        tasks = []
        for item in range(1, self.count + 1):
            t = self.req(item)
            task = asyncio.create_task(t)
            tasks.append(task)
        await asyncio.wait(tasks)
        await self.file()

    async def init(self):
        url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36"
        }
        data = {
            "cname": "北京",
            "pid": "",
            "pageIndex": "1",
            "pageSize": "10"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, data=data) as req:
                req = await req.json(content_type='text/plain', encoding='utf-8')
                self.count = math.ceil(req["Table"][0]["rowcount"] / 10)

    async def req(self, item):
        url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36"
        }
        data = {
            "cname": "北京",
            "pid": "",
            "pageIndex": item,
            "pageSize": "10"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, data=data) as req:
                req = await req.json(content_type='text/plain', encoding='utf-8')
                self.arr.append(req["Table1"])

    async def file(self):
        async with aiofiles.open("./" + "temp" + '.csv', "w", encoding="utf-8") as f:
            for item in self.arr:
                for i in item:
                    await f.write(str(i["rownum"]))
                    await f.write(",")
                    await f.write(i["storeName"])
                    await f.write(",")
                    await f.write(i["addressDetail"])
                    await f.write("\n")


if __name__ == '__main__':
    a = default_timer()

    main = Main()
    asyncio.run(main.run())

    b = default_timer()
    print(b - a)
