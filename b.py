from Crypto.Cipher import AES
import base64
import requests
import json


def aes(key, iv, data):
    key = key.encode("utf-8")
    iv = iv.encode("utf-8")
    data = data.encode("utf-8")

    b = 16 - (len(data) % 16)
    data += (chr(b) * b).encode("utf-8")

    cipher = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
    encrypt = cipher.encrypt(data)
    result = base64.b64encode(encrypt).decode()
    return result


if __name__ == '__main__':
    d = {"ids": "[3308080]", "level": "standard", "encodeType": "aac", "csrf_token": ""}
    d = json.dumps(d)
    key1 = "0CoJUm6Qyw8W8jud"
    i = "UBGC5NDAd83tTcEP"
    iv = "0102030405060708"

    temp = aes(key1, iv, d)
    encText = aes(i, iv, temp)
    encSecKey = "80f191336dd4fc6d66679418a551ff6bf7c274d741ef7e278dae34b94eb009fe3cd290f5fdbf73d8793cd8374852891eac75686d02dd2ec490e96eaff485ba0888ba5ccef63b28576824078d89c7ec37e8abe5074c7caea917f9871e777b2560b1af20313ef636668e0609be9c67273cfe5df6f474f86e3cc37687c8f21cc388"

    data = {"params": encText, "encSecKey": encSecKey}
    url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded",
    }

    req = requests.post(url=url, headers=headers, data=data)
    req.close()
    print(req)
    print(req.text)
