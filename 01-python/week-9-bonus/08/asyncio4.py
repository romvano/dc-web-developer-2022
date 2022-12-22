import asyncio
import time


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(3)
    print(f'{time.ctime()} Goodbye!')
    loop.stop()


def blocking():
    time.sleep(6)
    print(f"{time.ctime()} Hello from a thread!")


async def run_blocking():
    await loop.run_in_executor(None, blocking)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.create_task(main())
loop.create_task(run_blocking())
loop.run_forever()
tasks = asyncio.all_tasks(loop=loop)
group = asyncio.gather(*tasks, return_exceptions=False)
loop.run_until_complete(group)
loop.close()