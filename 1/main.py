import asyncio
import math
from timeit import default_timer

import aiofiles
import aiohttp
import requests


class Main:
    def __init__(self):
        self.arr = []
        self.count = None

    async def run(self):
        await self.init()
        # tasks = []
        # for item in range(1, self.count + 1):
        #     t = self.req(item)
        #     task = asyncio.create_task(t)
        #     tasks.append(task)
        # await asyncio.wait(tasks)
        # await self.file()

    async def init(self):
        url = "https://www.nmpa.gov.cn/datasearch/data/nmpadata/countNums"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Cookie": "token=; STEP_TIPS_INDEX=true; STEP_TIPS_RESULT=true; acw_tc=3ccdc15d16820637842478471e6b4f12f9b3ad9178e06ad40c780f104affef",
            "sign": "eea7bfc0b201303c89f01c034856cc52",
            "timestamp": "1682065227000",
        }
        data = {
            "itemIds": "ff8080817dff44ef017e08e778be02a8",
            "searchValue": "*",
            "isSenior": "N",
            "timestamp": "1682065227000"
        }
        req = requests.get(url=url, headers=headers,params=data)
        req = req.json()
        print(req)

    async def aioreq(self, item):
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

    async def aiofile(self):
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
    main = Main()
    asyncio.run(main.run())
