# -*- coding: utf-8 -*-

import os


print 'Process (%s) start ...' % os.getpid()
pid = os.fork()
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getpid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)


##由于Windows没有fork调用，上面的代码在Windows上无法运行。
##由于Mac系统是基于BSD（Unix的一种）内核，
##所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
