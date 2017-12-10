# -*- coding: utf-8 -*-

from urllib.request import urlopen
import json

##html = urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
##hjson = json.loads(html.read())
##print(hjson)


def fetch_data(url):
    html = urlopen(url)
    hjson = json.loads(html.read())
    return hjson

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data['query']['results']['channel']['location']['city'] == 'Beijing')


##利用urllib读取JSON，然后将JSON解析为Python对象
