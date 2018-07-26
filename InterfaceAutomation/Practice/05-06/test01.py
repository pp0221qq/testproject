# -*- coding:utf-8 -*-
# @Author : Emma
import requests
"""
url = "http://apis.juhe.cn/cook/query?key=63b40d5fefafe863d19c0a8f41ffaf3b&menu=%E8%A5%BF%E7%BA%A2%E6%9F%BF&rn=10&pn=3"
# r =requests.get(url)
r = requests.get(url)

"""
# 参数过多，可以将url和参数分开
url = "http://apis.juhe.cn/cook/query"
# 参数：key=63b40d5fefafe863d19c0a8f41ffaf3b&menu=%E8%A5%BF%E7%BA%A2%E6%9F%BF&rn=10&pn=3
par ={
    "key":"63b40d5fefafe863d19c0a8f41ffaf3b",
    "menu":"%E8%A5%BF%E7%BA%A2%E6%9F%BF",
    "rn":"10",
    "pn":"3"
    }
r = requests.get(url,params = par)
print(r.status_code)   # 1.状态码
print(r.headers)       # 2.返回的头部  字典是无序的
print(r.text)          # 3.返回的body


### 总结：Get请求两种方式：1.参数直接放到url里的？号后面；2. 参数单独取出来写成字典格式。
