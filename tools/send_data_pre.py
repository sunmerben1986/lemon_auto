import asyncio
import websockets
import json
import datetime


async def connect_to_websocket(request_all):
    host = "plemon.lemonstudio.tech:8443/b1341ad7830e502c957a07bbcf6fafd9/api/runtime/v1"
    parameter1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3V1aWQiOiI2MzhkYWJmOGM1MmY1YzJkOWRiZTUzMGJkZWU1MTYwMyIsImV4cCI6MTczMDkwNTQxMH0.OiQw8q3M5OLOVtIsB7mOyeIoB0DFJyErJl8S9BhrJIA"
    parameter2 = "52c174a0b7405f14b2e5ad1c7bf86134"
    parameter3 = 0
    parameter4 = 1699283089822
    parameter5 = "2e2362786ddf5251a5478a1c8f586392"
    
    url = f"wss://{host}/ws?token={parameter1}&tenant_uuid={parameter2}&device_type={parameter3}&SessionId={parameter4}&sid={parameter5}"
    async def consumer_handler(websocket):
        async for message in websocket:
            print(message)

    async with websockets.connect(url) as websocket:
        for req in request_all:
            event = asyncio.Event()
            await websocket.send(json.dumps(req))
            while True:
                response = await websocket.recv()
                await event.wait()