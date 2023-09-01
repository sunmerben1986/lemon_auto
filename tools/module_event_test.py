import asyncio
from websocket_utils import connect
import json
import sys
import os
import time
import random
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from page.module_obj import Module_obj as mo
from page.document_conf import module_event_before as mp
from tools.database import db, record


async def test_inline_sm():
    websocket = await connect()
    message_list = []
    moo = mo()
    message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list)])
    for message in message_list:
        await websocket.send(json.dumps(message))
        while True:
            response = await websocket.recv()
            res = await handle_message(response)
            if res is None:
                break
            elif res != 200 and len(res) == 32:            
                inline_create = moo.create_inline(mp.data_list, res)
                message_list.append(inline_create)
            elif res == 200:
                pass
            else:
                break
    await websocket.close()
    if isSucess(1, int(time.time())):
        return True
    else:
        return False
    
async def test_inline_sm_add():
    websocket = await connect()
    message_list = []
    moo = mo()
    message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list)])
    for message in message_list:
        await websocket.send(json.dumps(message))
        while True:
            response = await websocket.recv()
            res = await handle_message(response)
            if res is None:
                break
            elif res != 200 and len(res) == 32:            
                inline_create = moo.create_inline(mp.data_list, res)
                inline_data, item = set_inline_data(res, [mp.text1, mp.text2])
                inline_data = moo.add_inline_data(mp.data_list, res, inline_data)
                message_list.append(inline_create)
                message_list.append(inline_data)
            elif res == 200:
                pass
            else:
                break
    await websocket.close()
    if isSucess("save", item):
        return True
    else:
        return False
    
async def delete_inline_data():
    websocket = await connect()
    message_list = []
    moo = mo()
    message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list)])
    for message in message_list:
        await websocket.send(json.dumps(message))
        while True:
            response = await websocket.recv()
            res = await handle_message(response)
            if res is None:
                break
            elif res != 200 and len(res) == 32:            
                inline_create = moo.create_inline(mp.data_list, res)
                inline_data, item = set_inline_data(res, [mp.text1, mp.text2])
                inline_data = moo.add_inline_data(mp.data_list, res, inline_data)
                message_list.append(inline_create)
                message_list.append(inline_data)
            elif res == 200:
                pass
            else:
                break
    await websocket.close()
    if isSucess("save", item):
        return True
    else:
        return False

def isSucess(tag,item):
    db.connect()
    if tag == "create":
        record_data = record.select().where((record.编号 > item - 5) & (record.编号 < item + 5)).first()
    elif tag == "save":
        record_data = record.select().where(record.编号 == item, record.记录 == tag, record.前后 == "before").first()
    return record_data

def set_inline_data(inline_uuid, field_uuid_list):
    digits = "0123456789"
    ascii_letters = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str_list = [random.choice(digits +ascii_letters) for i in range(5)]
    random_str = ''.join(str_list)
    time_stamp = int(time.time())
    inline_data = {field_uuid_list[0]:time_stamp, field_uuid_list[1]:random_str}
    return inline_data, time_stamp

async def handle_message(message):
    message = json.loads(message)
    result = message.get("result")
    if result == 'on_open':
        return message.get("code")
    elif result == "create_page":
        return message.get("code")
    elif result == "component_event":
        v1 = message.get("data")["values"][0]
        v2 = v1.get("value")
        inline_list = v2.get("forms", [])
        if len(inline_list) != 0:
            return inline_list[0]

print(asyncio.run(test_inline_sm_add()))