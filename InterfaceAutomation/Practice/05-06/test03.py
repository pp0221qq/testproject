# -*- coding:utf-8 -*-
# @Author : Emma
import requests
url = "https://www.baidu.com"
r = requests.get(url)

# print(r.text)   # 有gzip这种，不能用text
print(r.content)  # 字节方式相应，自动解压gzip
print(r.url)      # 如果有重定向，则返回最后一个地址
print(r.cookies)  # 获取cookies


