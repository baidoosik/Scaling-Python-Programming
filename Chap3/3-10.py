'''

    asyncio는 일정 시간 후에 호출하는 방법을 제공.
    asyncio.sleep 으로 대기 루프를 만드는 대신, call_later와 call_at을
    사용해서 상대적으로 또는 절대적인 미래 시간에 함수를 호출한다!

'''
import asyncio


def hello_world():
    print("hello world")


loop = asyncio.get_event_loop()
loop.call_later(1, hello_world)
loop.run_forever()