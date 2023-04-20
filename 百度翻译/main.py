import asyncio
import base64
import json
from timeit import default_timer

import aiofiles
import aiohttp
import requests
from Crypto.Cipher import AES
from lxml import etree


class Main:
    def __init__(self):
        self.arr = []

    async def run(self):
        dw = ("dog", "cat")
        tasks = []
        for item in dw:
            t = self.req(item)
            task = asyncio.create_task(t)
            tasks.append(task)
        await asyncio.wait(tasks)
        await self.file()

    async def req(self, item):
        url = "https://fanyi.baidu.com/sug"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36"
        }
        data = {
            "kw": item
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, data=data) as req:
                req = await req.json()
                self.arr.append(req["data"][0])

    async def file(self):
        async with aiofiles.open("./" + "aaa" + '.csv', "w", encoding="utf-8") as f:
            for item in self.arr:
                await f.write(item["k"])
                await f.write(",")
                await f.write(item["v"])
                await f.write("\n")


if __name__ == '__main__':
    a = default_timer()

    main = Main()
    asyncio.run(main.run())

    b = default_timer()
    print(b - a)
