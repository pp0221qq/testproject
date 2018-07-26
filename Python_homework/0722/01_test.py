# -*- coding:utf-8 -*-
# @Author : Emma
class emma:
    def method01(input_key):
        "调用输出99乘法表，根据参数，控制输出形式（左上，左下，右上，右下）；"
        if input_key == 1:
            for i in range(1,10):
                for j in range(i,10):
                    print("%d*%d=%2d" %  (i,j,i*j),end = " ")
                print()
        elif input_key == 2:
            for i in range(1,10):
                for j in range(1,i+1):
                    print("%d*%d=%2d" %  (i,j,i*j),end = " ")
                print()
        elif input_key ==3:
            for i in range(1,10):
                for k in range(1,i):
                    print(end = "       ")
                for j in range(i,10):
                    print("%d*%d=%2d" %  (i,j,i*j),end = " ")
                print()
        elif input_key == 4:
            for i in range(1,10):
                for k in range(1,10-i):
                    print(end = "       ")
            for j in range(1,i+1):
                print("%d*%d=%2d" %  (i,j,i*j),end = " ")
            print()
        else:
            print("无效输入")
    method01(6)
def method02(sortingway):
    if sortingway ==1:




