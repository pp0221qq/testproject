#  coding=utf-8
#  coding:utf-8
#  -*- coding:utf-8 -*-

"""
如果一个数恰好等于它的因子之和，那这个数就是完全数，比如第一个数是6，
它的约数有1，2，3，6，除去6本身外6=1+2+3，第二个完全数是28=1+2+4+7+14，
那么问题来了:求出1000以内完全数
"""

# 方法1：
a = range(1,1000)
b = range(1,1000)
perfectnum = []
for i in a:
    temp=[]
    for j in b:
        if j<i:
            if not i%j:
                temp.append(j)
            else:
                continue
        else:
            break
    count = 0
    for m in temp:
        count=count+m
    if count==i:
        perfectnum.append(i)
    else:
        continue
print(perfectnum)

# 方法2

for i in range(1,1000):
    sum=0
    for k in range(1,i):
        if i%k==0:
            sum += k
    if i==s:
        print(i)
