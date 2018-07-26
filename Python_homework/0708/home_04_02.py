# -*- coding:utf-8 -*-
# @Author : Emma
# @File   : .py

# 输入一个数，输出它的幂
#i= int(input("请输入一个数："))
#print(i**i)


# 输出100以内的质数：
temp=[]
for i in range(2,100):
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      temp.append(i)
print(temp)


# 输出101-200之间的素数：
temp=[]
for i in range(101,201):
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      temp.append(i)
print("101-200之间的素数为：",temp)
print("素数的个数为：",len(temp))



