# -*- coding: utf-8 -*-

import hashlib

# 根据用户输入的口令， 计算出存储在数据库中的MD5口令。
def cacl_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
##print(cacl_md5('helloworld!'))

##======== RESTART: C:/Users/Administrator/Desktop/lxf/lxf16_hashlib.py ========
##420e57b017066b44e05ea1577f6e2e12
##>>>


# 验证用户登录
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}



def login(user, password):
    password_md5 = cacl_md5(password)
    return password_md5 == db[user]

print(login('michael','123456'))
print(login('bob','888888'))
print(login('alice','alice2008'))
