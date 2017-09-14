from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from citycode import citycode

prefix = 'http://www.weather.com.cn/weather1d/'
suffix = '.shtml'
city_id = (citycode["厦门"])

url = prefix + str(city_id) + suffix
#print(url)

htmldoc = urlopen(url)

soup = BeautifulSoup(htmldoc,"html.parser")

soup1 = soup.find('div','t')
#print(soup1)
soup_div = soup1.ul

weather_text = soup_div.get_text()
print(weather_text)
#group = re.findall(r'".*?"',weather_text)

#for i in group:
    #print(i)

#soup_div = re.compile(r'^var observe24h_data (.*?)}}$',htmldoc)
#print(soup_div)
