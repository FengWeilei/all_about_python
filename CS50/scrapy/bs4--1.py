Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(html_doc)

Warning (from warnings module):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\lib\site-packages\bs4\__init__.py", line 181
    markup_type=markup_type))
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <string>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "html.parser")

>>> soup = BeautifulSoup(html_doc,"html.parser")
>>> soup.prettify
<bound method Tag.prettify of 
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body></html>>
>>> soup.prettify()
'<html>\n <head>\n  <title>\n   The Dormouse\'s story\n  </title>\n </head>\n <body>\n  <p class="title">\n   <b>\n    The Dormouse\'s story\n   </b>\n  </p>\n  <p class="story">\n   Once upon a time there were three little sisters; and their names were\n   <a class="sister" href="http://example.com/elsie" id="link1">\n    Elsie\n   </a>\n   ,\n   <a class="sister" href="http://example.com/lacie" id="link2">\n    Lacie\n   </a>\n   and\n   <a class="sister" href="http://example.com/tillie" id="link3">\n    Tillie\n   </a>\n   ;\nand they lived at the bottom of a well.\n  </p>\n  <p class="story">\n   ...\n  </p>\n </body>\n</html>'
>>> soup.title
<title>The Dormouse's story</title>
>>> soup.title.name
'title'
>>> soup.title.string
"The Dormouse's story"
>>> soup.title.parent.name
'head'
>>> soup.p
<p class="title"><b>The Dormouse's story</b></p>
>>> soup.p['class']
['title']
>>> soup.a
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
>>> soup.findall('a')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    soup.findall('a')
TypeError: 'NoneType' object is not callable
>>> soup.find_all('a')
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
>>> soup.findAll('a')
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
>>> soup.find(id="link3")
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
>>> for link in soup.find_all('a'):
	print(link.get('href'))

	
http://example.com/elsie
http://example.com/lacie
http://example.com/tillie
>>> print(soup.get_text())

The Dormouse's story

The Dormouse's story
Once upon a time there were three little sisters; and their names were
Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.
...

>>> soup = BeautifulSoup(open(index.html))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    soup = BeautifulSoup(open(index.html))
NameError: name 'index' is not defined
>>> from urllib.request import urlopen

>>> from bs4 import BeautifulSoup
>>> html = urlopen("http://www.pythonscraping.com/pages/page2.html")

>>> bsobj = BeautifulSoup(html.read())

>>> print(bsobj.h1)

<h1>An Interesting Title</h1>
>>> 
