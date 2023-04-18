import time
import json
import execjs
import base64
import requests


def hex_md5(r):
    with open('./VM3920.js') as f:  # 执行 JS 文件
        ctx = execjs.compile(f.read())
        return ctx.call('hex_md5', r)


def aaa(r):
    with open('./VM325.js') as f:  # 执行 JS 文件
        ctx = execjs.compile(f.read())
        return ctx.call('aaa',r)


def py2Z4jszGf():
    appId = 'b4f94ed2a35f97737e783799d0384ae8'
    clienttype = 'WEB'
    # timestamp = int(time.time() * 1000)
    timestamp = 1681817484910
    method = 'GETDATA'
    obj = {
        "city": "深圳"
    }
    param = {
        "appId": appId,
        "method": method,
        "timestamp": timestamp,
        "clienttype": clienttype,
        "object": obj,
        "secret": hex_md5(
            appId + method + str(timestamp) + clienttype + json.dumps(obj, ensure_ascii=False, separators=(',', ':')))

    }
    a = json.dumps(param, ensure_ascii=False, separators=(',', ':'))
    param = base64.b64encode(a.encode('utf-8')).decode()
    param=aaa(param.encode("utf-8"))
    return param
print(py2Z4jszGf())

# url = "https://www.aqistudy.cn/apinew/aqistudyapi.php"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
# }
# data = {
#     "h4vGmZPQZ": py2Z4jszGf()
# }
# req = requests.post(url=url, headers=headers, data=data, verify=False)
# print(req)
# print(req.text)
