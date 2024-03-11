import asyncio
import websockets
import json
import datetime
from send_data import start_websocket_client
import asyncio

# You can import the function from the file and use it in another python file like this:


request_all = [{"command":"create_page","data":{"page":"3034b345a79c58c59bf2b9568010301b","context":{}}}, 
               {"command":"component_event","data":{"component":"0a4c35060e61575c81cd3ca5f2ab7451","event":"9ceef9dcd6da11ea8a7f84c5a603df26","params":{}}},
               {"command":"component_event","data":{"component":"0a4c35060e61575c81cd3ca5f2ab7451","event":"a62c193b7c9b5ef0aaa3b97a5204fa64","params":{"inline_sm":"f8638b937d095c3c84d09edeed0820aa"}}},
               {"command":"component_event","data":{"component":"f8638b937d095c3c84d09edeed0820aa","event":"572cfd2ee16e11ea8aef84c5a603df26","params":{"field":"39ab1cc8a6ab539e8929fc9e022b4177","value":"333"}}},
               {"command":"component_event","data":{"component":"0a4c35060e61575c81cd3ca5f2ab7451","event":"24f35cb716aa5045a7d17048e65eb11c","params":{"inline_row_data":{"f8638b937d095c3c84d09edeed0820aa":{"d81458726cca51218ec2eba21d849b7e":"222","39ab1cc8a6ab539e8929fc9e022b4177":"333"}}}}}] 

if __name__ == "__main__":
    asyncio.run(start_websocket_client(request_all))

if __name__ == "__main__":
    asyncio.run(start_websocket_client(request_all))
async def connect_to_websocket(request_all):
    host = "tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/runtime/v1"
    parameter1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3V1aWQiOiI1MWRiNWE4Nzg0YzA1ZmQwYjY0NGQ0NzA3M2Q2MTFkYSIsImV4cCI6MTcyNDkzMjEyNn0.GXt3FCa3aqcUGwhiPUbjyqgUH46cKUp7cR9OKO8gajE"
    parameter2 = "b858071bb83c5aa0bd9a40ce09572d9e"
    parameter3 = 0
    parameter4 = 1693310669915
    parameter5 = "0681ebe843dd56ea957270b9fcf2b21c"
    
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
                if response:
                    print(f"Received: {response}")
                    event.set()
                    break
                




request_all = [{"command":"create_page","data":{"page":"3034b345a79c58c59bf2b9568010301b","context":{}}}, 
               {"command":"component_event","data":{"component":"0a4c35060e61575c81cd3ca5f2ab7451","event":"9ceef9dcd6da11ea8a7f84c5a603df26","params":{}}},
               {"command":"component_event","data":{"component":"0a4c35060e61575c81cd3ca5f2ab7451","event":"a62c193b7c9b5ef0aaa3b97a5204fa64","params":{"inline_sm":"f8638b937d095c3c84d09edeed0820aa"}}},
               {"command":"component_event","data":{"component":"f8638b937d095c3c84d09edeed0820aa","event":"572cfd2ee16e11ea8aef84c5a603df26","params":{"field":"39ab1cc8a6ab539e8929fc9e022b4177","value":"333"}}},
               {"command":"component_event","data":{"component":"0a4c35060e61575c81cd3ca5f2ab7451","event":"24f35cb716aa5045a7d17048e65eb11c","params":{"inline_row_data":{"f8638b937d095c3c84d09edeed0820aa":{"d81458726cca51218ec2eba21d849b7e":"222","39ab1cc8a6ab539e8929fc9e022b4177":"333"}}}}}]

# asyncio.run(connect_to_websocket(request_all))
# task = asyncio.get_event_loop().create_task(connect_to_websocket(request_all))
# # 这里会一直等待 task
# asyncio.get_event_loop().run_until_complete(asyncio.wait([task]))
# asyncio.get_event_loop().run_forever()