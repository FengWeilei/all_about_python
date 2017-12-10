# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
from lxf35_hello import application

# 负责启动WSGI服务器

# 创建一个服务器，IP地址为空，端口是8000， 处理函数是application
httpd = make_server('', 8000, application)
print('Server HTTP on port 8000...')

# 开始监听HTTP请求
httpd.serve_forever()