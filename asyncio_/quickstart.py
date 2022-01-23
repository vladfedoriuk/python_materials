# quickstart.py
#  Asyncio Walk-through

import asyncio
import time


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


def blocking():
    time.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread!")


# asyncio.run(main())
loop = asyncio.get_event_loop()
"""
get_event_loop()  will  give  you  the  same
loop  instance  each  time,  as  long  as  you’re  using  only  a  single  thread. If  you’re
inside  an  async  def  function,  you  should  call  asyncio.get_running_loop()
instead,  which  always  gives  you  what  you  expect."""
task = loop.create_task(main())
loop.run_in_executor(None, blocking)
loop.run_until_complete(task)
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
