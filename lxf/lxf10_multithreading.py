#-*- coding: utf-8 -*-

import time, threading

balance = 0

def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(6,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


##>>> 
##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf10_multithreading.py ====
##12
##>>> 
##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf10_multithreading.py ====
##-11
##>>> 
##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf10_multithreading.py ====
##1
##>>> 
##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf10_multithreading.py ====
##-11
##>>> 
##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf10_multithreading.py ====
##11
##>>> 
##==== RESTART: C:/Users/Administrator/Desktop/lxf/lxf10_multithreading.py ====
##10
##>>>
