# -*- coding:utf-8 -*-
# @Author : Emma
import requests
url = "http://hi.haidilao.com/logins/login.action"
h = {
    "Content-Type": "application/x-www-form-urlencoded"
    }
body = {
        "userSchema.nickname":"1870677048",
        "typeHide":"2",
        "userSchema.pwd":"qq112233"
        }
r = requests.post(url,headers=h,data=body)
print(r.status_code)
print(r.text)

