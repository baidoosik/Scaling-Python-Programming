import asyncio


async def hello_world():
    print("hello_world")


async def hello_python():
    print("hello Python!")
    await asyncio.sleep(0.1)

event_loop = asyncio.get_event_loop()

try:
    result = event_loop.run_until_complete(asyncio.gather(
        hello_python(),
        hello_world()
    ))
    print(result)
finally:
    event_loop.close()


# asyncio.time 은 비동기 방식이기 때문에 지정된 시간까지 대기하는 동안 다른 일을 할 수 있다.
