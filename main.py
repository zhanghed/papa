import requests
import json
import time
import os
import ctypes

url = 'https://cn.bing.com'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1111111111; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
}
params = {
    'format': 'js',
    'idx': '0',
    'n': '1111111111',
    'nc': int(round((time.time()) * 1000)),
    'pid': 'hp',
}

if __name__ == '__main__':
    try:
        # 第一次
        req = requests.get(url=url + '/HPImageArchive.aspx', headers=headers, params=params)
        temp = json.loads(req.text)  # 将json格式字符串转化为对 象
        temp = temp['images'][0]
        name = temp['fullstartdate']  # 图片名称
        url_new = temp['url']  # 图片url
        # 第二次
        req = requests.get(url=url + url_new, headers=headers)
        with open(name + '.jpg', 'wb') as f:
            f.write(req.content)
        req.close()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(name + '.jpg'), 0)
        time.sleep(1)
        os.remove(name + '.jpg')
    except Exception as e:
        print(e)
