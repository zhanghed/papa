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
            r'<div class="hd">.*?<a href="(?P<url>.*?)" class="">.*?<span class="title">(?P<title>.*?)</span>', re.S)

        for i in rr.finditer(req.text):
            arr.append((i.group("title"), i.group("url")))

        req.close()

    with open('top250.csv', 'w',encoding="utf-8") as f:
        for item in arr:
            for i in item:
                f.write(str(i))
                f.write(",")
            f.write("\n")

