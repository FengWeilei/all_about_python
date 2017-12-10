# -*- coding: utf-8 -*-

import time, sys, queue
from multiprocessing.manager import BaseManager


class QueueManager(BaseManager):
    pass

# 这个QueueManager只从网上获取Queue， 所以注册时只提供名字：
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')


#连接到服务器，也就是运行task_master.py的机器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

# 端口验证码保持与task_master.py设置的完全一致：
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

#从网络连接
m.connect()

#获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()


for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

print('wirker exit.')


# Some bugs still exist
