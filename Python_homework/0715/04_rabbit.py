# -*- coding:utf-8 -*-
# @Author : Emma
# 有一对兔子，从出生后第三个月起，每个月都生一对兔子，小兔子长到第三个月后，每个月又生一对兔子，
# 假如兔子不死，问每个月的兔子总数为多少？
# 思路：设当前第i个月，这个月的兔子总数，大致可以分为2部分，1部分是非新生的，另一部分是当月新生的。
# 非新生的应该是第i-1个月的兔子总数，新生的取决于第i-2个月的兔子总数。即兔子[i]=兔子[i-1]+兔子[i-2]。
# 于是，各个月的兔子数就形成了一个斐波那契数列：斐波那契数列指的是这样一个数列：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
def rabbit(month):
    rabbits = [1,1] #初始值可自定义
    for i in range(1,month-1):
        if month < 3:
            break
        else:
            x = rabbits[i-1] + rabbits[i]
            rabbits.append(x)
    return rabbits
if __name__ == "__main__":
    print(rabbit(10))


