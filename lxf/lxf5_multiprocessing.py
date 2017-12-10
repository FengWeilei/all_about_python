# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

def run_pro(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_pro, args=('test',))
    print('Process will start.')
    p.start()
    p.join()
    print('Process end.')


# python3

# execute this in the terminal
