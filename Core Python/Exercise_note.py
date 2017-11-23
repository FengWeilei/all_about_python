Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2.
2.0
>>> type(0)
<class 'int'>
>>> type(.34)
<class 'float'>
>>> type(dir)
<class 'builtin_function_or_method'>
>>> data = "<class 'builtin_function_or_method'>"
>>> patt
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    patt
NameError: name 'patt' is not defined
>>> patt = r'<type \'[w+_]\''
>>> import re
>>> m = re.search(patt, data)
>>> m
>>> patt = r'<type [w+_]'
>>> m = re.search(patt, data)
>>> m
>>> patt = r"[0-9]{2}:[0-9]{2}:[0-9]{2}"
>>> data = "Wed Mar 14 05:47:12 1979::xdsu@shuuybupl.gov::290209632-4-9"
>>> m = re.search(patt, data)
>>> m
<_sre.SRE_Match object; span=(11, 19), match='05:47:12'>
>>> m.group()
'05:47:12'
>>> patt = r"\w+@\w+\.gov"
>>> m = re.search(patt, data).group()
>>> patt = r"\w+@\w+"
>>> m = re.search(patt, data).group()
>>> m
'xdsu@shuuybupl'
>>> patt = r"\w+@\w+\.gov"
>>> m = re.search(patt, data).group()
>>> m
'xdsu@shuuybupl.gov'
>>> patt = r"\w+@\w+\.(gov|edu|com)"
>>> m = re.search(patt, data).group()
>>> m
'xdsu@shuuybupl.gov'
>>> patt = "\d{4}$"
>>> m = re.search(patt, data).group()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    m = re.search(patt, data).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> patt = "w+[0-9]{4}$"
>>> m = re.search(patt, data).group()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    m = re.search(patt, data).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> patt = "w+[0-9]{4}"
>>> m = re.search(patt, data).group()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    m = re.search(patt, data).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> patt = r"w+[0-9]{4}"
>>> m = re.search(patt, data).group()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    m = re.search(patt, data).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> daat
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    daat
NameError: name 'daat' is not defined
>>> data
'Wed Mar 14 05:47:12 1979::xdsu@shuuybupl.gov::290209632-4-9'
>>> patt = r"\w+[0-9]{4}"
>>> m = re.search(patt, data).group()
>>> m
'290209632'
>>> patt = r"[\w\s]+[0-9]{4}"
>>> m = re.search(patt, data).group()
>>> m
'12 1979'
>>> patt = r"[\w\s:]+[0-9]{4}"
>>> 
>>> m = re.search(patt, data).group()
>>> m
'Wed Mar 14 05:47:12 1979'
>>> patt = r"\d{4}"
>>> m = re.search(patt, data).group()
>>> m
'1979'
>>> 
>>> patt = r"\d{2}:\d{2}\d{2}"
>>> m = re.search(patt, data).group()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    m = re.search(patt, data).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> patt = r"\d{2}:\d{2}:\d{2}"
>>> m = re.search(patt, data).group()
>>> m
'05:47:12'
>>> data
'Wed Mar 14 05:47:12 1979::xdsu@shuuybupl.gov::290209632-4-9'
>>> patt = r"\w+@\w+\.(gov|edu|com|org)"
>>> m = re.findall(patt, data)
>>> m
['gov']
>>> patt = r"\w+@\w+\.(gov|edu|com|org)"
>>> m = re.search(patt, data)
>>> m
<_sre.SRE_Match object; span=(26, 44), match='xdsu@shuuybupl.gov'>
>>> m.group()
'xdsu@shuuybupl.gov'
>>> m = re.search(patt, data).group()
>>> m
'xdsu@shuuybupl.gov'
>>> patt = r"(\w+)@\w+\.(gov|edu|com|org)"
>>> m = re.search(patt, data).group(1)
>>> m
'xdsu'
>>> patt = r"(\w+)@(\w+)\.(gov|edu|com|org)"
>>> m = re.search(patt, data).groups()
>>> m
('xdsu', 'shuuybupl', 'gov')
>>> patt = r"(\w+)@(\w+\.gov|edu|com|org)"
>>> m = re.search(patt, data).groups()
>>> m
('xdsu', 'shuuybupl.gov')
>>> re.sub(r"(\w+)@(\w+\.gov|edu|com|org)",'18790166674@163.com')
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    re.sub(r"(\w+)@(\w+\.gov|edu|com|org)",'18790166674@163.com')
TypeError: sub() missing 1 required positional argument: 'string'
>>> re.sub(r"(\w+)@(\w+\.gov|edu|com|org)",r'18790166674@163.com')
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    re.sub(r"(\w+)@(\w+\.gov|edu|com|org)",r'18790166674@163.com')
TypeError: sub() missing 1 required positional argument: 'string'
>>> re.sub(r"(\w+)@(\w+\.gov|edu|com|org)",r"18790166674@163.com")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    re.sub(r"(\w+)@(\w+\.gov|edu|com|org)",r"18790166674@163.com")
TypeError: sub() missing 1 required positional argument: 'string'
>>> help(re.sub)
Help on function sub in module re:

sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the match object and must return
    a replacement string to be used.

>>> re.sub(r"(\w+)@(\w+\.gov|edu|com|org)",r"18790166674@163.com", data)
'Wed Mar 14 05:47:12 1979::18790166674@163.com::290209632-4-9'
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
>>> help(os.popen)
Help on function popen in module os:

popen(cmd, mode='r', buffering=-1)
    # Supply os.popen()

>>> help(os.open)
Help on built-in function open in module nt:

open(path, flags, mode=511, *, dir_fd=None)
    Open a file for low level IO.  Returns a file descriptor (integer).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.

>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/1_27.py", line 4, in <module>
    with os.open('redata.txt','r') as f:
TypeError: an integer is required (got type str)
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/1_27.py", line 4, in <module>
    with os.open('redata.txt') as f:
TypeError: Required argument 'flags' (pos 2) not found
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/1_27.py", line 4, in <module>
    f = open('redata.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'redata.txt'
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/1_27.py", line 4, in <module>
    f = open(r'C:\Users\Administrator\Desktop\redata.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Administrator\\Desktop\\redata.txt'
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
Tue May 31 03:28:10 2022::cqoxrh@qybasmx.edu::1653938890-6-7

Wed Jan 22 05:06:30 1997::qgypa@vwdxabhi.edu::853880790-5-8

Wed Mar 14 05:47:12 1979::xdsu@shuuybupl.gov::290209632-4-9

Thu Apr 09 16:09:25 2009::mchxvi@iynvdmmt.edu::1239264565-6-8

Sun Aug 25 19:18:09 1996::aitfioq@pbqptglipouk.edu::840971889-7-12

Sun Mar 14 08:32:13 1982::xdoka@znkrksj.gov::384913933-5-7

Tue Jul 25 17:51:27 2006::tlnzq@rjphsortxtdl.gov::1153821087-5-12

Sun May 08 15:32:01 2022::mejur@iicjqowng.gov::1651995121-5-9
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/1_27.py", line 6, in <module>
    MDY = re.findall(patt, eachline)
NameError: name 'eachline' is not defined
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
[('May', '31', '2')]
[('Jan', '22', '7')]
[('Mar', '14', '9')]
[('Apr', '09', '9')]
[('Aug', '25', '6')]
[('Mar', '14', '2')]
[('Jul', '25', '6')]
[('May', '08', '2')]
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
[('May', '31', '2')]
[('Jan', '22', '7')]
[('Mar', '14', '9')]
[('Apr', '09', '9')]
[('Aug', '25', '6')]
[('Mar', '14', '2')]
[('Jul', '25', '6')]
[('May', '08', '2')]
>>> 
============== RESTART: C:/Users/Administrator/Desktop/1_27.py ==============
[('May', '31', '2022')]
[('Jan', '22', '1997')]
[('Mar', '14', '1979')]
[('Apr', '09', '2009')]
[('Aug', '25', '1996')]
[('Mar', '14', '1982')]
[('Jul', '25', '2006')]
[('May', '08', '2022')]
>>> patt = '\((\d{3})\)?|(\d{3}-)?\d{3}-\d{4}'
>>> data = (800)555-1212.
SyntaxError: invalid syntax
>>> data = "(800)555-1212"
>>> re.match(patt, data)
<_sre.SRE_Match object; span=(0, 5), match='(800)'>
>>> re.match(patt, data).group()
'(800)'
>>> re.match(patt, data).groups()
('800', None)
>>> patt = '(\((\d{3})\)?|(\d{3}-)?)\d{3}-\d{4}'
>>> re.match(patt, data).groups()
('(800)', '800', None)
>>> re.match(patt, data).group()
'(800)555-1212'
>>> patt = '(\((\d{3})\)?|(\d{3}-)?)\d{3}-\d{4}'
>>> data = "(800)555-1212"
>>> re.match(patt, data).group()
'(800)555-1212'
>>> 
