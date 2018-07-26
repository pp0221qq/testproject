#  -*- coding:utf-8 -*-
# @Author : Emma
# 2.输入一个数字，按照排序顺序插入到列表中
# 随机生成n个数字
import random
m = int(input("请选择想要进行几个数字的排序："))
numslist = random.sample(range(1,100),m)
print("随机生成的数字为：",numslist)

# 输入想要插入的数字
n = int(input("请输入想要插入的数字："))

# 将输入的数字插入原来的列表中
numslist.append(n)
list1 = numslist
print("插入之后的列表为：",list1)
# 排序
for i in range(m+1):
    for j in range(m):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
        #else:

print("排序之后的列表为：",list1)




