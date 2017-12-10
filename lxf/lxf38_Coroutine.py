# -*- coding utf-8 -*-

def consumer():    # generator
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Comsuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PEODUCE] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCE] Comsumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
