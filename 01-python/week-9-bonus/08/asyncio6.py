import asyncio
import time


async def f():
    print("f")
    await asyncio.sleep(1.0)
    print("f end")
    loop.stop()
    return 123

async def main():
    print("main")
    result = await f()
    print("main end", result)
    return result


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.create_task(main())
loop.run_forever()
tasks = asyncio.all_tasks(loop=loop)
group = asyncio.gather(*tasks, return_exceptions=False)
loop.run_until_complete(group)