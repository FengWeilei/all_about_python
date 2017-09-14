# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 10:20:28 2017

@author: Administrator
"""


import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib.request
import time

urlpage = "http://www.meizitu.com/a/5390.html"

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


html = requests.get(urlpage)
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36"}
session = requests.session()
session.headers.update(headers)


html = session.get(urlpage,headers=headers)
soup = BeautifulSoup(html.content,"lxml")
img_tag = soup.find('div',id="picture").find_all("img")
#print(img_tag)

for i in range(len(img_tag)):
    img_url = img_tag[i]['src']
    img_name = img_tag[i]['alt']
    
    path = 'F:\\meizitu\\'+img_name+'.jpg'
    urlretrieve(img_url,path)
    time.sleep(1)
    print("正在下载第"+str(i+1)+"张图片")
    