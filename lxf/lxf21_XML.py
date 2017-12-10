# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib.request import urlopen

result = {}
L = []
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        
        if name == 'yweather:location':
            result['city'] = attrs['city']
##            print(attrs['city'])
         
        if name == 'yweather:forecast':
            Li = {}
            Li['date'] = attrs['date']
            Li['high'] = attrs['high']
            Li['low'] = attrs['low']

            L.append(Li)
##            print(L,Li)
        result['forecast'] = L
        

            


    def end_element(self, name):
        pass

    def char_data(self, text):
        pass

url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with urlopen(url, timeout=4) as f:
    xml = f.read()


def parseXml():
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return result

result = parseXml()

print(result)
print(result['city'] == 'Beijing')


##xml = r'''<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2017-12-09T06:58:28Z" yahoo:lang="zh-CN">
##<results>
##<channel>
##<yweather:units xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" distance="mi" pressure="in" speed="mph" temperature="F"/>
##<title>Yahoo! Weather - Beijing, Beijing, CN</title>
##<link>
##http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/
##</link>
##<description>Yahoo! Weather for Beijing, Beijing, CN</description>
##<language>en-us</language>
##<lastBuildDate>Sat, 09 Dec 2017 02:58 PM CST</lastBuildDate>
##<ttl>60</ttl>
##<yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="Beijing" country="China" region=" Beijing"/>
##<yweather:wind xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" chill="45" direction="210" speed="11"/>
##<yweather:atmosphere xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" humidity="18" pressure="1009.0" rising="0" visibility="16.1"/>
##<yweather:astronomy xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" sunrise="7:24 am" sunset="4:49 pm"/>
##<image>
##<title>Yahoo! Weather</title>
##<width>142</width>
##<height>18</height>
##<link>http://weather.yahoo.com</link>
##<url>
##http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif
##</url>
##</image>
##<item>
##<title>
##Conditions for Beijing, Beijing, CN at 02:00 PM CST
##</title>
##<geo:lat xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">39.90601</geo:lat>
##<geo:long xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">116.387909</geo:long>
##<link>
##http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/
##</link>
##<pubDate>Sat, 09 Dec 2017 02:00 PM CST</pubDate>
##<yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="Sat, 09 Dec 2017 02:00 PM CST" temp="48" text="Sunny"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="09 Dec 2017" day="Sat" high="48" low="25" text="Partly Cloudy"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="10 Dec 2017" day="Sun" high="41" low="29" text="Sunny"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="11 Dec 2017" day="Mon" high="33" low="22" text="Mostly Sunny"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="12 Dec 2017" day="Tue" high="28" low="16" text="Mostly Sunny"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="13 Dec 2017" day="Wed" high="31" low="13" text="Mostly Sunny"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="28" date="14 Dec 2017" day="Thu" high="31" low="14" text="Mostly Cloudy"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="15 Dec 2017" day="Fri" high="38" low="17" text="Partly Cloudy"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="16 Dec 2017" day="Sat" high="36" low="21" text="Mostly Sunny"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="17 Dec 2017" day="Sun" high="36" low="17" text="Sunny"/>
##<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="18 Dec 2017" day="Mon" high="38" low="23" text="Mostly Sunny"/>
##<description>
##<![CDATA[<img src="http://l.yimg.com/a/i/us/we/52/32.gif"/> <BR /> <b>Current Conditions:</b> <BR />Sunny <BR /> <BR /> <b>Forecast:</b> <BR /> Sat - Partly Cloudy. High: 48Low: 25 <BR /> Sun - Sunny. High: 41Low: 29 <BR /> Mon - Mostly Sunny. High: 33Low: 22 <BR /> Tue - Mostly Sunny. High: 28Low: 16 <BR /> Wed - Mostly Sunny. High: 31Low: 13 <BR /> <BR /> <a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/">Full Forecast at Yahoo! Weather</a> <BR /> <BR /> <BR /> ]]>
##</description>
##<guid isPermaLink="false"/>
##</item>
##</channel>
##</results>
##</query>
##<!--  total: 4  -->
##'''
