#  -*- coding:utf-8 -*-
# @Author : 飘飘_emmm
# 1.定义一个函数，实现冒泡排序
# 随机生成n个数字
import random
n = int(input("请选择想要进行几个数字的排序："))
numslist = random.sample(range(1,100),n)
print("随机生成的数字为：",numslist)
# 排序
for i in range(n):
    for j in range(i):
        if numslist[j]>numslist[j+1]:
            numslist[j],numslist[j+1]=numslist[j+1],numslist[j]
print("排序之后的数字为：",numslist)
