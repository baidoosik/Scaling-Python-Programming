'''

    네트워크 서버

    asyncio 는 수천 개의 네트워크 연결을 다루는 데 탁월하므로 네트워크 서버를 구현할 때 유용한 프레임워크를 제공한다.

    aiohttp를 사용해서 asyncio 기반 웹 서버를 만들 수 있다. 그렇지만 uwsgi나 gunicorn같은 빠르고 최적화된 기본 wsgi

    서버보다 느리므로 그다지 쓸 만하지 않다. 파이썬 웹 애플리케이션은 항상 WSGI 를 사용하므로 빠른 비동기 방식으로 WSGI 서버를

    전환하기는 쉽다.

'''
import time
import asyncio

SERVER_ADDRESS = ('127.0.0.1', 1234)


class YellEchoServer(asyncio.Protocol):
    def __init__(self, stats):
        self.stats = stats
        self.stats['started at'] = time.time()

    def connection_made(self, transport):
        self.tranport = transport
        self.stats['connections'] += 1

    def data_received(self, data):
        self.tranport.write(data.upper())
        self.stats['message sent'] +=1

    def connection_lost(self, exc):
        print("Client disconnected")


event_loop = asyncio.get_event_loop()

stats = {
    "started at": time.time(),
    "connections": 0,
    "message sent": 0
}
factory = event_loop.create_server(
    lambda: YellEchoServer(stats), *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)

try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    event_loop.close()

    ran_for = time.time() - stats['started at']
    print("Server ran for: %.2f seconds" % ran_for)
    print("Connections: %d" % stats['connections'])
    print("Message sent: %d" % stats['message sent'])
    print("Messages sent per second: %.2f" % (stats["message sent"] /ran_for))
