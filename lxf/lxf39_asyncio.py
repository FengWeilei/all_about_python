# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def hello():
    print('Hello World!')
    r = yield from asyncio.sleep(1)  # 异步调用asyncio.sleep(1)
    print('Hello again!')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()



# await async  代码更简洁
async def hello():
    print('Hello world!')
    r = await asyncio.sleep(1)
    print('Hello again')
