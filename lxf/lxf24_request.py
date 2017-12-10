# -*- coding: utf-8 -*-

import requests

r = requests.get('https://www.douban.com/')
##print(r.status_code)
##print(r.headers)
##print(r.headers['Content-Type'])
##print(r.text)


##r = requests.get('https://www.douban.com/search', params={'q':'python', 'cat':'1001'})
##print(r.url)
##print(r.encoding)
##print(r.content)


##r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
##print(r.json())


##r = requests.get('https://www.douban.com/', headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
##print(r.text)


### POST请求
##r = requests.post('https://accounts.douban.com/login', \
##                  data={'form_email':'abc@example.com', 'password':'123456'})


#上传文件
##upload_files = {'file': open('report.xls', 'rb')}  # 二进制上传、读取
##r = requests.post(url, files=upload_files)


##cs = {'token':'12345', 'status':'working'}
##url = 'https://www.douban.com/'
##r = requests.get(url,cookies=cs)  # 请求中上传一个cookie


##r = requests.get(url, timeout=2.5 # 设置2.5秒后超时

