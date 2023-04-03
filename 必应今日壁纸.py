import requests
import time

url1 = "https://cn.bing.com/HPImageArchive.aspx"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1111111111; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
}
data = {
    'format': 'js',
    'idx': '1',
    'n': '999',
    'nc': int(round((time.time()) * 1000)),
    'pid': 'hp',
}

req = requests.get(url=url1, headers=headers, params=data)
req = req.json()

for i in req["images"]:
    name = i['title']
    url2 = "https://cn.bing.com" + i['url']
    req = requests.get(url=url2, headers=headers)
    with open(name + '.jpg', 'wb') as f:
        f.write(req.content)

req.close()
