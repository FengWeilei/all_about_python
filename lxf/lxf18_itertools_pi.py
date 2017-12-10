# -*- coding: utf-8 -*-

import itertools

def pi(N):
    L1 = itertools.count(1, 2)
    L2 = []
    for i in L1:
        if i < 2*N:
            L2.append(i)
        else:
            break
    L3 = []
    Length = len(L2)
    for j in range(Length):
        if j %2 == 0:
            L3.append(4/L2[j])
        else:
            L3.append(-4/L2[j])
    return sum(L3)
    
            
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
