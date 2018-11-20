import asyncio
import threading

@asyncio.coroutine
def hello():
    print('Hello World! (%s)' % threading.currentThread())
    r = yield from asyncio.sleep(5)
    print('Hello Again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()