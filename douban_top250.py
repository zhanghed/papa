import requests, re

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36",
}
data = {
    "start": "",
}

if __name__ == '__main__':
    arr = []
    for item in range(10):
        data["start"] = str(item)
        req = requests.get(url=url, headers=headers, params=data)
        req.encoding = "utf-8"

        rr = re.compile(
            r'<a href="(?P<url>.*?)" class="">\n                            <span class="title">(?P<title>.*?)</span>')

        for i in rr.finditer(req.text):
            arr.append((i.group("title"), i.group("url")))

    print(arr, len(arr))
