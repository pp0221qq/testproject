# -*- coding:utf-8 -*-
# @Author : Emma
import requests
import urllib3
urllib3.disable_warnings()

url = "https://www.baidu.com/"

r = requests.get(url,verify=False)  # verify=False  不校验证书
print(r.status_code)

