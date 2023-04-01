import requests, re

url = "https://movie.douban.com/j/chart/top_list"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36",
}
data = {
    "type": "13",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}
req = requests.get(
    url=url,
    headers=headers,
    params=data
)
# req = requests.get(
#     url=url,
#     headers=headers,
#     data=data
# )

req.encoding = "utf-8"
print(req)

# print(req.text)
# print(req.json())

rr = re.compile(r'"title":"(?P<title>.*?)","url":"(?P<url>.*?)","release_date":')
for i in rr.finditer(req.text):
    print(i.group("title"), i.group("url"))
