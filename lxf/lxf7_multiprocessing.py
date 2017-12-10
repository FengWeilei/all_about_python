# -*- coding: utf-8 -*-

import subprocess

print('$ nalookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)


# execute this in the terminal
