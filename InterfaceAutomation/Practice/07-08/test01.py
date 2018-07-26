# -*- coding:utf-8 -*-
# @Author : Emma
import  requests
url = "https://mp.csdn.net/postedit"
r1 = requests.get(url)
print(r1.status_code)
print(r1.url)