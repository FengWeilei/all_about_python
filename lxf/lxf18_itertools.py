# -*- coding: utf-8 -*-

import itertools


##natuals = itertools.count(1)  # 无限迭代器
##for n in natuals:
##    print(n)


##cs = itertools.cycle('ABC')  #会把一个序列无限重复下去。
##for c in cs:
##    print(c)


##ns = itertools.repeat('A',3) # 把一个元素无限重复下去， 第二个参数限制次数
##for i in ns:
##    print(i)


##for c in itertools.chain('ABC','XYZ'):   #把一组对象串联起来，一起迭代
##    print(c)


##for key, group in itertools.groupby('AAABBBCCAAA'):  # 把迭代器中相邻的重复元素挑出来放在一起
##    print(key, list(group))


for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))    # 通过函数挑选的，这里忽略大写小
