# -*- coding:utf-8 -*-
# @Author : Emma
import requests
url = "http://zzk-s.cnblogs.com/s/blogpost?Keywords=yoyo"
h = {
    "Cookie":"AspxAutoDetectCookieSupport=1"
    }
r = requests.get(url,headers=h)
print(r.status_code)
print(r.headers)
print(r.text)
