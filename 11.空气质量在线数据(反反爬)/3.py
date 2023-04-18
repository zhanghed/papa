import time
import json
import execjs
import base64


def hex_md5(r):
    with open('./VM3920.js') as f:  # 执行 JS 文件
        ctx = execjs.compile(f.read())
        return ctx.call('hex_md5', r)


def py2Z4jszGf():
    appId = '73f1bec004d0347d09dcc6c6c9a2a82c'
    clienttype = 'WEB'
    # timestamp = str(int(time.time() * 1000))
    timestamp = "1681808090176"
    method = 'GETDATA'
    obj = {
        "city": "郑州"
    }
    param = {
        "appId": appId,
        "method": method,
        "timestamp": timestamp,
        "clienttype": clienttype,
        "object": obj,
        "secret": hex_md5(
            appId + method + timestamp + clienttype + json.dumps(obj, ensure_ascii=False, separators=(',', ':')))

    }
    a=json.dumps(param, ensure_ascii=False, separators=(',', ':'))
    b=a.encode('utf-8')
    print(str(b,'utf-8'))
    param = base64.b64encode(b).decode()
    return param

# eyJhcHBJZCI6IjczZjFiZWMwMDRkMDM0N2QwOWRjYzZjNmM5YTJhODJjIiwibWV0aG9kIjoiR0VUREFUQSIsInRpbWVzdGFtcCI6MTY4
# MTgwODA5MDE3NiwiY2xpZW50dHlwZSI6IldFQiIsIm9iamVjdCI6eyJjaXR5Ijoi6YOR5beeIn0sInNlY3JldCI6IjdjNWZiYzJhMDhm
# OWEzMDdkMzIxOWYxNjAwYmJlNjgzIn0=

print(py2Z4jszGf())



# var py2Z4jszGf = (function() {
#
#     function ObjectSort(obj) {
#         var newObject = {};
#         Object.keys(obj).sort().map(function(key) {
#             newObject[key] = obj[key];
#         });
#         return newObject;
#     }
#     return function(method, obj) {
#         var appId = '364f12f0a30c5b89a01f4bd801ab86e4';
#         var clienttype = 'WEB';
#         var timestamp = new Date().getTime();
#         // console.log(method, obj,ObjectSort(obj),appId + method + timestamp + 'WEIXIN' + JSON.stringify(ObjectSort(obj)));
#         var param = {
#             appId: appId,
#             method: method,
#             timestamp: timestamp,
#             clienttype: clienttype,
#             object: obj,
#             secret: hex_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
#         };
#         param = BASE64.encrypt(JSON.stringify(param));
#         param = DES.encrypt(param, dckT6p5BRXYq, dciLUy2PqYMv);
#         return param;
#     }
#     ;
# }
# )();
