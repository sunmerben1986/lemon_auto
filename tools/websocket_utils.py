import asyncio
import websockets
import json

async def connect():
    host = "tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/runtime/v1"
    parameter1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3V1aWQiOiI1MWRiNWE4Nzg0YzA1ZmQwYjY0NGQ0NzA3M2Q2MTFkYSIsImV4cCI6MTczMTA3NjUxMH0.09upeK9YBcfEAFnQs-aZlAIzNZKtbSVWdFZk4NpFZdk"
    parameter2 = "b858071bb83c5aa0bd9a40ce09572d9e"
    parameter3 = 0
    parameter4 = 1699778379198
    parameter5 = "0681ebe843dd56ea957270b9fcf2b21c"
    
    url = f"wss://{host}/ws?token={parameter1}&tenant_uuid={parameter2}&SessionId={parameter4}&device_type={parameter3}"

    websocket = await websockets.connect(url)
    return websocket

async def send_request(websocket, message):
    await websocket.send(json.dumps(message))
    while True:
        response = await websocket.recv()
        print(response)