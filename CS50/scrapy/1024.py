# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 22:56:25 2017

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib.request
import time


opener=urllib.request.build_opener()

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

urlpage = "http://cl.b8y.xyz/htm_data/7/1708/2609950.html"
html = requests.get(urlpage)
#print(html.headers)


soup = BeautifulSoup(html.content,"lxml")
img_tag = soup.find('div',class_="tpc_content do_not_catch").find_all("img")
print(img_tag)

#try:
#    for i in range(len(img_tag)):
#        time.sleep(1)
#        img_url = img_tag[i]['src']
#        img_name = str(i)
#        
#        path = 'F:\\1024\\'+img_name+'.jpg'
#        
#        print(img_url)
#except:
#    print("Error")