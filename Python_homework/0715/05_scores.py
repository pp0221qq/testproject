# -*- coding:utf-8 -*-
# @Author : Emma
# 从键盘输入10个学生的成绩并存储在列表中，求成绩最高者、最低者的序号和成绩
scores = input("请输入10个学生的成绩，以逗号分隔：")             # 输入成绩
slist = scores.split(",")  # 将字符串以逗号分隔开
slist = [int(slist[i]) for i in range(len(slist))]
print(slist)
# 找出最小成绩
for i in range(0,len(slist)):
    for j in range(0,i+1):
        if slist[i]>slist[j]:
            slist[i],slist[j]=slist[j],slist[i]
print(slist[len(slist)-1])
print(slist[0])









