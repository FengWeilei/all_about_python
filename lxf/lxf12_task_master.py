# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列：
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上，callable参数关联了Queue对象：
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口5000， 设置验证码'abc'
manager = QueueManager(address=('',5000), authkey=b'abc')

# 启动Queue
manager.start()

#获得通过网络访问的Queue对象：
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

print('Try get result...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' %r)

manager.shutdown()
print('master exit.')



# Some bugs still exist


# 重要的不是什么都会，而是什么都能很快上手






