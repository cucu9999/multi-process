import asyncio
import aiohttp
import blog_spider
import time

async def  async_craw(url):
    print(f"crawing {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            # print(f"craw {url}, {len(result)}")

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls
]

start_time = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print(f"time cost:{end_time - start_time}")


