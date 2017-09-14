Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Unicode（）
SyntaxError: invalid character in identifier
>>> unicode(22)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    unicode(22)
NameError: name 'unicode' is not defined
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')

Warning (from warnings module):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\lib\site-packages\bs4\__init__.py", line 181
    markup_type=markup_type))
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <string>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "html.parser")

>>> soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>',"html")
>>> soup.a
<a rel="index">homepage</a>
>>> soup.a.string
'homepage'
>>> sou.a.string.unicode()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    sou.a.string.unicode()
NameError: name 'sou' is not defined
>>> soup.a.string.unicode()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    soup.a.string.unicode()
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\lib\site-packages\bs4\element.py", line 737, in __getattr__
    self.__class__.__name__, attr))
AttributeError: 'NavigableString' object has no attribute 'unicode'
>>> unicode(soup.a.string)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    unicode(soup.a.string)
NameError: name 'unicode' is not defined
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
>>> tag2 = soup.p
>>> tag2
<p>Back to the <a rel="index">homepage</a></p>
>>> tag2.string
>>> tag2 = soup.a
>>> tag.string
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tag.string
NameError: name 'tag' is not defined
>>> tag2.string
'homepage'
>>> type(tag2.string)
<class 'bs4.element.NavigableString'>
>>> 
>>> markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
>>> soup3 = BeautifulSoup(makeup)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    soup3 = BeautifulSoup(makeup)
NameError: name 'makeup' is not defined
>>> soup3 = BeautifulSoup(markup)
>>> comment = soup.b.string
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    comment = soup.b.string
AttributeError: 'NoneType' object has no attribute 'string'
>>> soup.b
>>> comment = soup3.b.string
>>> comment
'Hey, buddy. Want to buy a used parser?'
>>> soup.b.prettify
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    soup.b.prettify
AttributeError: 'NoneType' object has no attribute 'prettify'
>>> soup3.b.prettify
<bound method Tag.prettify of <b><!--Hey, buddy. Want to buy a used parser?--></b>>
>>> soup3.b.prettify()
'<b>\n <!--Hey, buddy. Want to buy a used parser?-->\n</b>'
>>> from bs4 import CData
>>> cdata = CData("Paranoia")
>>> comment.rep
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    comment.rep
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\lib\site-packages\bs4\element.py", line 737, in __getattr__
    self.__class__.__name__, attr))
AttributeError: 'Comment' object has no attribute 'rep'
>>> comment.replace_with(cdata)
'Hey, buddy. Want to buy a used parser?'
>>> soup3
<b><![CDATA[Paranoia]]></b>
>>> soup3.b.prettify()
'<b>\n <![CDATA[Paranoia]]>\n</b>'
>>> 
