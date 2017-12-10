# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



##======== RESTART: C:/Users/Administrator/Desktop/lxf/lxf40_asyncio.py ========
##wget www.163.com...   # 先打印了这三句，然后再打印其他头部信息
##wget www.sina.com.cn...
##wget www.sohu.com...
##www.163.com header > HTTP/1.0 302 Moved Temporarily
##www.163.com header > Server: Cdn Cache Server V2.0
##www.163.com header > Date: Sun, 10 Dec 2017 07:59:49 GMT
##www.163.com header > Content-Length: 0
##www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
##www.163.com header > Connection: close
##www.sohu.com header > HTTP/1.1 200 OK
##www.sohu.com header > Content-Type: text/html;charset=UTF-8
##www.sohu.com header > Connection: close
##www.sohu.com header > Server: nginx
##www.sohu.com header > Date: Sun, 10 Dec 2017 07:58:56 GMT
##www.sohu.com header > Cache-Control: max-age=60
##www.sohu.com header > X-From-Sohu: X-SRC-Cached
##www.sohu.com header > Content-Encoding: gzip
##www.sohu.com header > FSS-Cache: HIT from 9796327.17595121.11133278
##www.sohu.com header > FSS-Proxy: Powered by 3373701.4749967.4710554
##www.sina.com.cn header > HTTP/1.1 200 OK
##www.sina.com.cn header > Server: nginx
##www.sina.com.cn header > Date: Sun, 10 Dec 2017 07:59:50 GMT
##www.sina.com.cn header > Content-Type: text/html
##www.sina.com.cn header > Content-Length: 604383
##www.sina.com.cn header > Connection: close
##www.sina.com.cn header > Last-Modified: Sun, 10 Dec 2017 07:57:05 GMT
##www.sina.com.cn header > Vary: Accept-Encoding
##www.sina.com.cn header > Expires: Sun, 10 Dec 2017 08:00:49 GMT
##www.sina.com.cn header > Cache-Control: max-age=60
##www.sina.com.cn header > X-Powered-By: shci_v1.03
##www.sina.com.cn header > Age: 1
##www.sina.com.cn header > Via: http/1.1 ctc.ningbo.ha2ts4.97 (ApacheTrafficServer/6.2.1 [cRs f ]), http/1.1 ctc.shanghai.ha2ts4.131 (ApacheTrafficServer/6.2.1 [cMsSf ])
##www.sina.com.cn header > X-Via-Edge: 1512892789436ef661e75601c49de40ada0bd
##www.sina.com.cn header > X-Cache: MISS.131
##www.sina.com.cn header > X-Via-CDN: f=edge,s=ctc.shanghai.ha2ts4.132.nb.sinaedge.com,c=117.30.102.239;f=Edge,s=ctc.shanghai.ha2ts4.131,c=222.73.3.132;f=edge,s=ctc.ningbo.ha2ts4.83.nb.sinaedge.com,c=222.73.3.131;f=Edge,s=ctc.ningbo.ha2ts4.97,c=115.238.190.83
##>>> 
