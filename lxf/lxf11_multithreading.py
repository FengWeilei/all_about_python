#-*- coding: utf-8 -*-

import time, threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(100000):
        lock.acquire()  # 获得锁
        try:
            change_it(n)
        finally:
            lock.release()  # 释放锁

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(6,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf11_multithreading.py ====
##0
##>>> 
##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf11_multithreading.py ====
##0
##>>> 
##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf11_multithreading.py ====
##0
##>>> 
##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf11_multithreading.py ====
##0
##>>> 
