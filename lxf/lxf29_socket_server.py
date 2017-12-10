# -*- coding: utf-8 -*-

import socket
import time
import threading

# 创建一个基于IPv4和TCP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定监听的地址和端口
s.bind(('127.0.0.1',9999))  # '127.0.0.1' 本机地址，客户端必须同时在本机运行才能连接

s.listen(5) # 调用listen()来开始监听端口，参数5 指定等待连接的最大数量
print('waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:  # 创建一个永久循环来接受来自客户端的连接
    sock, addr = s.accept()  # 等待并返回一个客户端的连接
    # 创建新进程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))  
    t.start()


