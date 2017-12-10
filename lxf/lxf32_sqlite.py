# -*- coding: utf-8 -*-

import sqlite3

# 连接数据库（test.db文件），文件不存在，在当前目录会创建一个
conn = sqlite3.connect('test.db')

# 需要打开游标cursor,通过Cursor来执行SQL语句
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 这里执行了一条SQL语句，创建了一个user表
# user表有两列，第一列id，设置为主键，可以唯一确定一行数据 varchar 可变字符

cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount) # 获得插入的行数

cursor.close()  #关闭cursor
conn.commit()  #提交数据
conn.close() # 断开连接


