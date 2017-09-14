import requests
from bs4 import BeautifulSoup
import urllib.request as a

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER"}
session = requests.session()
session.headers.update(headers)

urlpage = "https://www.qiushibaike.com/text/page/2/?s=5000302"
html = session.get(urlpage,headers=headers)
#print(html.content)


soup = BeautifulSoup(html.content,"html.parser")
text_tag = soup.find_all('div',class_="content")
print(text_tag)

##for i in range(len(img_tag)):
##    img_url = img_tag[i]['src']
##    img_name = img_tag[i]['alt']
##    
##    path = 'F:\\meizitu\\'+img_name+'.jpg'
##    a.urlretrieve(img_url,path)
##    
##    picture = requests.get(img_url).content
##    with open(path,'bw') as file:
##        file.write(picture)
