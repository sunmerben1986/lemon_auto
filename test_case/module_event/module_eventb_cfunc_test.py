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
from page.document_conf import fe_module_eventb as fmp
from tools.database import db, record, module_eventb_tmp


#云函数触发模型保存事件，保存前触发
async def test_cloud_save():
    websocket = await connect()
    message_list = []
    moo = mo()
    message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list), moo.btn_event(mp.page_uuid, mp.save_btn)])
    for message in message_list:
        await websocket.send(json.dumps(message))
        await asyncio.sleep(1)
    await websocket.close()
    item = int(time.time())
    if isSucess("cloud_save", item):
        return True
    else:
        return False

#云函数触发模型删除事件，删除前触发
async def test_cloud_func_delete():
    websocket = await connect()
    message_list = []
    moo = mo()
    pk_list = get_pk_list()
    message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list), moo.btn_event(mp.page_uuid, mp.delete_btn)])
    for message in message_list:
        await websocket.send(json.dumps(message))
        await asyncio.sleep(1)
    await websocket.close()
    time_stamp = int(time.time())
    if isSucess("cloud_delete", time_stamp):
        return True
    else:
        return False
    
#云函数更新模型数据，数据不存在，保存前触发
async def test_update_unexist_data():
    websocket = await connect()
    message_list = []
    moo = mo()
    pk_dict = get_pk_dict()
    message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list), moo.btn_event(mp.page_uuid, mp.update1_btn)])
    for message in message_list:
        await websocket.send(json.dumps(message))
        await asyncio.sleep(1)
    await websocket.close()
    time_stamp = int(time.time())
    if isSucess("cloud_save", time_stamp):
        return False
    else:
        return True

#云函数更新模型数据，数据存在，保存前触发
async def test_update_exist_data():
    websocket = await connect()
    message_list = []
    moo = mo()
    pk_dict = get_pk_dict()
    message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list), moo.btn_event(mp.page_uuid, mp.update2_btn)])
    for message in message_list:
        await websocket.send(json.dumps(message))
        await asyncio.sleep(1)
    await websocket.close()
    time_stamp = int(time.time())
    if isSucess("cloud_delete", time_stamp):
        return True
    else:
        return False

def isSucess(tag,item):
    db.connect()
    if tag == "cloud_delete":
        record_data = record.select().where((record.编号 > item - 10) & (record.编号 < item + 5)).first()
    elif tag == "cloud_save":
        record_data = record.select().where(((record.编号 > item - 10) & (record.编号 < item + 5)), record.记录 == tag, record.前后 == "before").first()
    return record_data

def get_pk_list():
    db.connect()
    pks = module_eventb_tmp.select(module_eventb_tmp.id)
    pk_list = []
    for pk in pks:
        pk_list.append(pk.id)
    db.close()
    return pk_list

def get_pk_dict():
    db.connect()
    pk = module_eventb_tmp.select(module_eventb_tmp.id).first()
    pk_dict = {"pk": pk}
    db.close()
    return pk_dict

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

print(asyncio.run(test_cloud_save()))