import asyncio
import time


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(5)
    print(f'{time.ctime()} Goodbye!')
    loop.stop()

def blocking():
    print("blocking started")
    time.sleep(3)
    print(f"{time.ctime()} Hello from a thread!")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

loop.create_task(main())
loop.run_in_executor(None, blocking)
loop.run_forever()

pending = asyncio.all_tasks(loop=loop)
group = asyncio.gather(*pending)
loop.run_until_complete(group)
loop.close()