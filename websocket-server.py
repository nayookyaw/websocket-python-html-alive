#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import time, json

async def hello(websocket, path):
    while True:
        # try:
        #     name = await websocket.recv()
        # except Exception as e:
        #     print (e)

        # print(f"< {name}")
        # greeting = f"Hello {name}!"
        # req = await websocket.recv()
        # print (json.load(req))

        greeting = "Hello from Server"
        res = {
            'msg' : 'connected',
            'version' : '1.0.1'
        }

        await websocket.send(json.dumps(res))

        print("Sending to client")
        await asyncio.sleep(1)

start_server = websockets.serve(hello, "localhost", 8765)
print ("Websocket Server is running")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()