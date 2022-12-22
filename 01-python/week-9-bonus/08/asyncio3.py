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


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

loop.create_task(main())

loop.run_in_executor(None, blocking)
loop.run_forever()
tasks = asyncio.all_tasks(loop=loop)
group = asyncio.gather(*tasks, return_exceptions=True)
loop.run_until_complete(group)
loop.close()