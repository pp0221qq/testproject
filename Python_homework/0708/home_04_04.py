# -*- coding:utf-8 -*-
# @Author : Emma

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
str = str(input("请输入一行字符："))
alpha = 0
space = 0
digit = 0
other = 0

for a in str:
    if a.isalpha():
        alpha += 1
    elif a.isspace():
        space += 1
    elif a.isdigit():
        digit += 1
    else:
        other += 1
print("%d,%d,%d,%d" % (alpha,space,digit,other))


