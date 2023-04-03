import requests, re

url = "https://www.dy2018.com/html/bikan/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36",
}
data = {

}

if __name__ == '__main__':
    req = requests.get(url=url, headers=headers, params=data)
    req.encoding = "gb2312"
    print(req.text)

    rr = re.compile(r'<a href=(?P<url>.*?) class="ulink" title=.*?>(?P<title>.*?)</a>', re.S)

    for i in rr.finditer(req.text):
        print((i.group("title"), i.group("url")))

    req.close()
