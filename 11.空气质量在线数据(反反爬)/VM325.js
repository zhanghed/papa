const  askX8qjp6xbs = "aCQhnwNJeTBDPf5D";//AESkey，可自定义
const  asi1XlcB9YVg = "bUcPXEWe5YdiG5fi";//密钥偏移量IV，可自定义

const  ackrmN6GrZ4R = "dlfffEegYSHRnHro";//AESkey，可自定义
const  acinGxrugeR3 = "fXFYHlNvT6lyG1ou";//密钥偏移量IV，可自定义

const  dskspBM7N4q3 = "hkWGSRFugObGUscp";//DESkey，可自定义
const  dsiVX3freQRd = "xyDwgFrIDdREDV30";//密钥偏移量IV，可自定义

const  dckhzESRNJVE = "oPea1irxHKZTrBlS";//DESkey，可自定义
const  dci9BIT5Eh7T = "pELIzoU7F2mUpQCZ";//密钥偏移量IV，可自定义

const aes_local_key = 'emhlbnFpcGFsbWtleQ==';
const aes_local_iv = 'emhlbnFpcGFsbWl2';

var BASE64 = {
    encrypt: function(text) {
        var b = new Base64();
        return b.encode(text);
    },
    decrypt: function(text) {
        var b = new Base64();
        return b.decode(text);
    }
};

var DES = {
 encrypt: function (text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.encrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
 },
 decrypt: function(text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.decrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
  }
};
function aaa(text){
return DES.encrypt(text, dckhzESRNJVE, dci9BIT5Eh7T)
}
var AES = {
  encrypt: function(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    // console.log('real key:', secretkey);
    // console.log('real iv:', secretiv);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.encrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
  },
  decrypt: function(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.decrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
  }
};

var localStorageUtil = {
  save: function(name, value) {
    var text = JSON.stringify(value);
    text = BASE64.encrypt(text);
    text = AES.encrypt(text, aes_local_key, aes_local_iv);
    try {
      localStorage.setItem(name, text);
    } catch (oException) {
      if (oException.name === 'QuotaExceededError') {
        // console.log('超出本地存储限额！');
        localStorage.clear();
        localStorage.setItem(name, text);
      }
    }
  },
  check: function(name) {
    return localStorage.getItem(name);
  },
  getValue: function(name) {
    var text = localStorage.getItem(name);
    var result = null;
    if (text) {
      text = AES.decrypt(text, aes_local_key, aes_local_iv);
      text = BASE64.decrypt(text);
      result = JSON.parse(text);
    }
    return result;
  },
  remove: function(name) {
    localStorage.removeItem(name);
  }
};

// console.log('base64', BASE64.encrypt('key'));

function dfcmu88FCwo(pjviW4X) {
  pjviW4X = DES.decrypt(pjviW4X, dskspBM7N4q3, dsiVX3freQRd);
  return pjviW4X;
}

function dcmfwXbHeL(pjviW4X) {
  pjviW4X = AES.decrypt(pjviW4X, askX8qjp6xbs, asi1XlcB9YVg);
  return pjviW4X;
}

function gsVo2J6YBIKAFGKF(key, period) {
    if (typeof period === 'undefined') {
        period = 0;
    }
    var d = DES.encrypt(key);
    d = BASE64.encrypt(key);
    var data = localStorageUtil.getValue(key);
    if (data) { // 判断是否过期
        const time = data.time;
        const current = new Date().getTime();
        if (new Date().getHours() >= 0 && new Date().getHours() < 5 && period > 1) {
            period = 1;
        }
        if (current - (period * 60 * 60 * 1000) > time) { // 更新
           data = null;
        }
        // 防止1-5点用户不打开页面，跨天的情况
        if (new Date().getHours() >= 5 && new Date(time).getDate() !== new Date().getDate() && period === 24) {
           data = null;
        }
    }
    return data;
}

function ObjectSort(obj) {
    var newObject = {};
    Object.keys(obj).sort().map(function(key){
      newObject[key] = obj[key];
    });
    return newObject;
}
function dAShgwW2IEF1Bp903FF2RkP(data) {
    data = AES.decrypt(data, askX8qjp6xbs, asi1XlcB9YVg);
    data = DES.decrypt(data, dskspBM7N4q3, dsiVX3freQRd);
    data = BASE64.decrypt(data);
    return data;
}
var pGBpEN6wBPQaTj = (function(){

function ObjectSort(obj){
    var newObject = {};
    Object.keys(obj).sort().map(function(key){
        newObject[key] = obj[key];
    });
    return newObject;
}
return function(method, obj){
    var appId = 'b4f94ed2a35f97737e783799d0384ae8';
    var clienttype = 'WEB';
    var timestamp = new Date().getTime();
    // console.log(method, obj,ObjectSort(obj),appId + method + timestamp + 'WEIXIN' + JSON.stringify(ObjectSort(obj)));
    var param = {
      appId: appId,
      method: method,
      timestamp: timestamp,
      clienttype: clienttype,
      object: obj,
      secret: hex_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
    };
    param = BASE64.encrypt(JSON.stringify(param));
    param = DES.encrypt(param, dckhzESRNJVE, dci9BIT5Eh7T);
    return param;
};
})();

function syZQjVjQLTkNwzp8(mIprBYKu6, omJe9GCvrF, cu4AtAEFF, p2ejoTH) {

    const ksRt = hex_md5(mIprBYKu6 + JSON.stringify(omJe9GCvrF));

    const dc43h = gsVo2J6YBIKAFGKF(ksRt, p2ejoTH);
    if (!dc43h) {
      var pjviW4X = pGBpEN6wBPQaTj(mIprBYKu6, omJe9GCvrF);
        $.ajax({
            url: '../apinew/aqistudyapi.php',
            data: { hGHe0S5tr: pjviW4X },
            type: "post",
            success: function (dc43h) {
                dc43h = dAShgwW2IEF1Bp903FF2RkP(dc43h);
                oPPko9 = JSON.parse(dc43h);
                if (oPPko9.success) {
                    if (p2ejoTH > 0) {
                      oPPko9.result.time = new Date().getTime(); // 添加当前时间
                      localStorageUtil.save(ksRt, oPPko9.result);
                    }
                    cu4AtAEFF(oPPko9.result);
                } else {
                    console.log(oPPko9.errcode, oPPko9.errmsg);
                }
            }
        });
    } else {
        cu4AtAEFF(dc43h);
    }
}