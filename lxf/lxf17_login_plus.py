# -*- coding: utf-8 -*-

import hashlib

# 模拟注册
db = {}

def register(username, password):
    def get_md5(s):
        md5 = hashlib.md5()
        md5.update(s.encode('utf-8'))
        return md5.hexdigest()
    db[username] = get_md5(password + username +'the-Salt')


# 根据修改后的MD5算法实现用户登录的验证：
import random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


print(login('michael', '123456'))
print(login('michael', '123456'))
print(login('bob', 'abc999'))
print(login('alice', 'alice2008'))
print(not login('michael', '1234567'))
print(not login('bob', '123456'))
print(not login('alice', 'Alice2008'))
