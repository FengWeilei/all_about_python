# -*- coding: utf-8 -*-

import socket

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))   # 连接新浪服务器

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    d = s.recv(1024)  # 每次最多接收1K字节
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close

header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))  # 打印头部信息

with open('sina.html', 'wb') as f:
    f.write(html)  # 网页本身写进sina.html
