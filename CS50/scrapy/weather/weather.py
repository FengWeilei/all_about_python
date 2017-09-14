from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from citycode import citycode

prefix = 'http://www.weather.com.cn/weather1d/'
suffix = '.shtml'
city_id = '101230206'
print(citycode["北京"])

url = prefix + city_id + suffix
#print(url)

htmldoc = urlopen(url)

soup = BeautifulSoup(htmldoc,"html.parser")

soup_div = soup.find_all(re.compile(r'^script'))
weather_text = soup_div[2].get_text()

group = re.findall(r'".*?"',weather_text)

#for i in group:
    #print(i)

#soup_div = re.compile(r'^var observe24h_data (.*?)}}$',htmldoc)
#print(soup_div)
