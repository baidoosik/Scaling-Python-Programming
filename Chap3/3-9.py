import asyncio
import aiohttp


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response

loop = asyncio.get_event_loop()

coroutines = [get("http://example.com") for i in range(8)]

results = loop.run_until_complete(asyncio.gather(*coroutines))

print("Asyncio Results: {}".format(results))
