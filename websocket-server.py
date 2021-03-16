#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import time, json

port = 8765

class initWebsocketServer:
    def start(self):
        start_server = websockets.serve(WebsocketServer.run, "localhost", port)
        print ("Websocket Server is running at ", port)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

class WebsocketServer:
    async def run(websocket, path):
        while True:
            # try:
            #     name = await websocket.recv()
            # except Exception as e:
            #     print (e)

            # print(f"< {name}")
            # greeting = f"Hello {name}!"
            # req = await websocket.recv()
            # print (json.load(req))
            try:
                greeting = "Hello from Server"
                res = {
                    'msg' : 'connected',
                    'version' : '1.0.1'
                }

                await websocket.send(json.dumps(res))

                print("Sending to client")
                await asyncio.sleep(1)
            except Exception as e:
                print (e)
                break

if __name__ == '__main__':
    initWebsocketServer = initWebsocketServer()
    initWebsocketServer.start()