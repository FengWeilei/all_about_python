# -*- coding: utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5.update('How to use md5 in Python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


##======== RESTART: C:/Users/Administrator/Desktop/lxf/lxf16_hashlib.py ========
##af22508f0ec78ee30dbf2acc62789ef1
##>>> 


sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

##======== RESTART: C:/Users/Administrator/Desktop/lxf/lxf16_hashlib.py ========
##af22508f0ec78ee30dbf2acc62789ef1
##2c76b57293ce30acef38d98f6046927161b46a44
##>>> 


# 根据用户输入的口令， 计算出存储在数据库中的MD5口令。
def cacl_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
print(cacl_md5('helloworld!'))

##======== RESTART: C:/Users/Administrator/Desktop/lxf/lxf16_hashlib.py ========
##420e57b017066b44e05ea1577f6e2e12
##>>> 
