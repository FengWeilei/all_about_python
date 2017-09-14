from urllib.request import urlopen
from bs4 import BeautifulSoup
from citycode import citycode


def get_weather(cityname):
    prefix = 'http://www.weather.com.cn/weather1d/'
    suffix = '.shtml'
    # 根据用户输入城市名找到对应的城市编码id
    city_id = citycode[cityname]

    #完整的URL
    url = prefix + str(city_id) + suffix

    htmldoc = urlopen(url)
    soup = BeautifulSoup(htmldoc,"html.parser")
    soup1 = soup.find('div','t')

    # 这是今天的天气信息
    result_almost = soup1.ul

    # 这样直接当最后结果，调用函数后返回这个结果
    result = result_almost.get_text()
    return result
