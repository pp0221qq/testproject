# -*- coding:utf-8 -*-
# @Author : Emma
import pymysql

# 连接数据库
conn= {
    'host':'140.143.203.54',
    'port':'3306',
    'user':'root',
    'password':'Test12345.',
    'db':'test',
    'charset':'utf8'
    }

print("Connection successfully")
# 通过cursor创建游标
cursor = conn.cursor()

# 创建sql语句，并执行
aa = cursor.execute("select languagename from languages")
print(aa)

# 使用 fetchall() 方法获取多条数据
data = cursor.fetchall()
for i in data:
    print(i)



# 关闭数据库连接
cursor.close()
print("Closed successfully")


