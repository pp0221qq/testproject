# -*- coding:utf-8 -*-
# @Author : Emma
# @File   : .py

# 输出基本乘法表：
for i in range(1,10):
    for j in range(1,10):
        print("%d*%d=%2d" %  (i,j,i*j),end = " ")
    print()

# 输出左上三角形乘法表：
for i in range(1,10):
    for j in range(i,10):
        print("%d*%d=%2d" %  (i,j,i*j),end = " ")
    print()

# 输出左下三角形乘法表：
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%2d" %  (i,j,i*j),end = " ")
    print()

# 输出右上三角形乘法表：
for i in range(1,10):
    for k in range(1,i):
        print(end = "       ")
    for j in range(i,10):
        print("%d*%d=%2d" %  (i,j,i*j),end = " ")
    print()
# 输出右下三角形乘法表：
for i in range(1,10):
    for k in range(1,10-i):
        print(end = "       ")
    for j in range(1,i+1):
        print("%d*%d=%2d" %  (i,j,i*j),end = " ")
    print()