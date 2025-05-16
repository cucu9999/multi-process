import asyncio
import aiohttp
import blog_spider
import time

async def  async_craw(url):
    # print(f"crawing {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            # print(f"craw {url}, {len(result)}")

loop = asyncio.get_event_loop() # 创建事件循环，可以理解为一个超级循环。

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls
]

start_time = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print(f"time cost:{end_time - start_time}")


# 并发度的调控
semaphore = asyncio.Semaphore(10) # 限制并发度为10

async def  async_craw(url):
    async with semaphore:
        # print(f"crawing {url}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                result = await response.text()
                # await asyncio.sleep(5) # 用于观察并发度的变化，每次都是应该都是10
                # print(f"craw {url}, {len(result)}")

loop_new = asyncio.get_event_loop() # 创建事件循环，可以理解为一个超级循环。

tasks = [
    loop_new.create_task(async_craw(url))
    for url in blog_spider.urls
]

start_time = time.time()
loop_new.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print(f"semaphored time cost:{end_time - start_time}")