# -*- coding: utf-8 -*-

# 编写一个 search(s) 的函数，能在当前目录的所有子目录下查找文件名
# 包含指定字符串的文件，并打印出完整路径

import os

basedir = os.path.abspath('.')
##print basedir

def search(s):
    for dirpath, dirnames, filenames in os.walk(basedir):
        for f in filenames:
            if f.find(s) != -1:
                absf = os.path.join(dirpath,f)
##                print dirpath,f
                print absf

search('test')



##>>> 'lxf3_search_test.py'.find('test')
##12
##>>> 


##>>> help(os.walk)
##Help on function walk in module os:
##
##walk(top, topdown=True, onerror=None, followlinks=False)
##    Directory tree generator.
##    
##    For each directory in the directory tree rooted at top (including top
##    itself, but excluding '.' and '..'), yields a 3-tuple
##    
##        dirpath, dirnames, filenames
##    
##    dirpath is a string, the path to the directory.  dirnames is a list of
##    the names of the subdirectories in dirpath (excluding '.' and '..').
##    filenames is a list of the names of the non-directory files in dirpath.
##    Note that the names in the lists are just names, with no path components.
##    To get a full path (which begins with top) to a file or directory in
##    dirpath, do os.path.join(dirpath, name).
