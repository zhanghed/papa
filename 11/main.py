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
        self.init()

    def init(self):
        url = "https://www.aqistudy.cn/apinew/aqistudyapi.php"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        }
        data = {
            "hXzfFHi83": "O5GbJ/LC82TgJPSScQ8B8DuP+/nuIeOQNtKYfyGukomIVyZGAx/15xrKMZ6vL1OV5Xhyq0MzqSGutRbPQOu/MeVMNxgKcTL3snl8c/Pod92wCnMSWdyud8kLglIEpg2DSDeMUaDoSl0OQtRAF5391MVOLR/eG3tU+XDfzvSxISdgIhTAo/8VLlPfsHnQ1vSkJb/FKX2VB8vFKKU3yx8RphIwhyCLRXKVMVfev+GLe1wS8m+aGc+fslv17Dz5T3DQ8eset/Ap7NCNNze0jk8ujskedfkWrPjazBGdgkXqzGAYY0ofiFZY4g0P7GfPPyrFRIDW1tijBM4="}
        req = requests.post(url=url, headers=headers, data=data, verify=False)
        print(req)
        print(req.text)

    def aes(self, key, iv, data):
        key = key.encode("utf-8")
        iv = iv.encode("utf-8")
        data = data.encode("utf-8")
        b = 16 - (len(data) % 16)
        data += (chr(b) * b).encode("utf-8")
        cipher = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
        encrypt = cipher.encrypt(data)
        result = base64.b64encode(encrypt).decode()
        return result

    async def run(self):
        d = {"ids": None, "level": "standard", "encodeType": "aac", "csrf_token": ""}
        key1 = "0CoJUm6Qyw8W8jud"
        key2 = "UBGC5NDAd83tTcEP"
        iv = "0102030405060708"
        data = {
            "params": None,
            "encSecKey": "80f191336dd4fc6d66679418a551ff6bf7c274d741ef7e278dae34b94eb009fe3cd290f5fdbf73d8793cd8374852891eac75686d02dd2ec490e96eaff485ba0888ba5ccef63b28576824078d89c7ec37e8abe5074c7caea917f9871e777b2560b1af20313ef636668e0609be9c67273cfe5df6f474f86e3cc37687c8f21cc388"
        }
        tasks = []
        for item in self.arr:
            d["ids"] = "[" + str(item["id"]) + "]"
            dd = json.dumps(d)
            temp = self.aes(key1, iv, dd)
            temp = self.aes(key2, iv, temp)
            data["params"] = temp
            t = self.download(item, data)
            task = asyncio.create_task(t)
            tasks.append(task)
        await asyncio.wait(tasks)

    async def download(self, item, data):
        url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, data=data) as req:
                req = await req.text()
                req = json.loads(req)
                req = req["data"][0]["url"]
                print(req)
                async with aiohttp.ClientSession() as session2:
                    async with session2.get(url=str(req), headers=headers) as req2:
                        req2 = await req2.content.read()
                        await self.file(item, req2)

    async def file(self, item, req):
        async with aiofiles.open("./temp/" + item["name"] + '.m4a', "wb") as f:
            await f.write(req)


if __name__ == '__main__':
    a = default_timer()

    main = Main()
    asyncio.run(main.run())

    b = default_timer()
    print(b - a)
