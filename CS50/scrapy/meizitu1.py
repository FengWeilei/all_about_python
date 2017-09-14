# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 23:39:07 2017

@author: Administrator
"""

from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import urllib.request

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

urlpage = "http://www.meizitu.com/a/5530.html"
html = requests.get(urlpage)
soup = BeautifulSoup(html.content,"lxml")
img_tag = soup.find('div',id="picture").find_all("img")
#print(img_tag)

for i in range(len(img_tag)):
    img_url = img_tag[i]['src']
    img_name = img_tag[i]['alt']
    
    path = 'F:\\pic_test\\'+img_name+'.jpg'
    urlretrieve(img_url,path)
    print("正在下载第"+str(i+1)+"张图片")