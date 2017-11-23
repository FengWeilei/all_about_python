Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> type(0)
<type 'int'>
>>> type(.34)
<type 'float'>
>>> type(dir)
<type 'builtin_function_or_method'>
>>> patt = r'<type \'[w+_]\''
>>> data = "<type 'builtin_function_or_method'>"
>>> import re
>>> re.search(patt, data)
>>> patt = 'type [w+_]'
>>> re.search(patt, data)
>>> re.search(patt, data).group()

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    re.search(patt, data).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> re.search('type',data)
<_sre.SRE_Match object at 0x01BC6C28>
>>> re.search('type',data).group()
'type'
>>> patt = r'<type \'[w+_]+\''
>>> re.search(patt,data).group()

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    re.search(patt,data).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> patt = r'<type [w+_]+'
>>> re.search(patt,data).group()

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    re.search(patt,data).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> patt = r'<type [A-Za-z_]+'
>>> re.search(patt,data).group()

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    re.search(patt,data).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> patt = 'type [A-Za-z_\']+'
>>> re.search(patt,data).group()
"type 'builtin_function_or_method'"
>>> patt = 'type ([A-Za-z_\']+)'
>>> re.search(patt,data).group()
"type 'builtin_function_or_method'"
>>> re.search(patt,data).group(1)
"'builtin_function_or_method'"
>>> patt = 'type \'([A-Za-z_\']+)\''
>>> re.search(patt,data).group(1)
'builtin_function_or_method'
>>> data = "<type 'builtin_function_or_method'>"
>>> import re
>>> patt = 'type \'([A-Za-z_\']+)\''
>>> re.search(patt,data).group(1)
'builtin_function_or_method'
>>> patt = '(0?[1-9])|1[0-2]'
>>> data = '12 23 10 09 9 6'
>>> re.search(patt,data).groups()
('1',)
>>> re.search(patt,data).group()
'1'
>>> re.findall(patt,data)
['1', '2', '2', '3', '1', '09', '9', '6']
>>> 
