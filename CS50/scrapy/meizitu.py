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

print("Enter the page you want to scrapy in 'http://www.meizitu.com'.")
print("Something like this: http://www.meizitu.com/a/5390.html ")
urlpage = input("Enter a page url:")

print("---"*20)
print("Enter the Folder path you prepared to save the picture.")
print("Something like this: F:\\pic_test ")
print("But make sure you created it already.")
Folder_path = input("Enter the Folder path:")


html = requests.get(urlpage)
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36"}
session = requests.session()
session.headers.update(headers)


html = session.get(urlpage,headers=headers)
soup = BeautifulSoup(html.content,"lxml")
img_tag = soup.find('div',id="picture").find_all("img")
#print(img_tag)


opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


for i in range(len(img_tag)):
    img_url = img_tag[i]['src']
    img_name = img_tag[i]['alt']
    
    path = Folder_path + '\\' + img_name + '.jpg'
    urlretrieve(img_url,path)
    time.sleep(1)
    print("正在下载第"+str(i+1)+"张图片")
    