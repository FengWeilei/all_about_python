# -*- coding: utf-8 -*-

import socket

# 创建Socket， AF_INET指定使用IPv4协议， SOCK_DGRAM指定Socket类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))# 绑定地址和端口 （不需要listen监听）

print('Bind UDP on 9999...')
while True:
    data, addr = s.recvfrom(1024)   # recvfrom()返回数据和客户端地址与端口
    print('Received from %s:%s' % addr)
    s.sendto(b'Hello, %s' %data, addr)  # 服务器收到数据等，再返回给客户端
    
