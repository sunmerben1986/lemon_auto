import asyncio
import json
import time
import unittest
from page.base_utils import base_utils as bu
from page.page_conf import module_event_after as mp, fe_module_eventa as fmp
from tools.database import db
from tools.websocket_utils import connect

class module_eventa_cfunc_test(unittest.IsolatedAsyncioTestCase):
    #云函数触发模型保存事件，保存后触发
    async def test_01_cloud_save(self):
        websocket = await connect()
        message_list = []
        moo = bu()
        message_list.extend([moo.create_page(mp.page_uuid), moo.base_event(mp.data_list,"event_inited"), moo.btn_event(mp.page_uuid, mp.save_btn)])
        for message in message_list:
            await websocket.send(json.dumps(message))
            await asyncio.sleep(1)
        await websocket.close()
        item = int(time.time())
        if moo.isSucess("cloud_save", item, "after"):
            return True
        else:
            return False

    #云函数触发模型删除事件，删除后触发
    async def test_04_cloud_func_delete(self):
        websocket = await connect()
        message_list = []
        moo = bu()
        message_list.extend([moo.btn_event(mp.page_uuid, mp.delete_btn)])
        for message in message_list:
            await websocket.send(json.dumps(message))
            await asyncio.sleep(1)
        await websocket.close()
        time_stamp = int(time.time())
        if moo.isSucess("cloud_delete", time_stamp, "after"):
            return True
        else:
            return False
        
    #云函数更新模型数据，数据不存在，保存后触发
    async def test_02_update_unexist_data(self):
        websocket = await connect()
        message_list = []
        moo = bu()
        message_list.extend([moo.btn_event(mp.page_uuid, mp.update1_btn)])
        for message in message_list:
            await websocket.send(json.dumps(message))
            await asyncio.sleep(1)
        await websocket.close()
        time_stamp = int(time.time())
        if moo.isSucess("cloud_save", time_stamp, "after"):
            return False
        else:
            return True

    #云函数更新模型数据，数据存在，保存后触发
    async def test_03_update_exist_data(self):
        websocket = await connect()
        message_list = []
        moo = bu()
        message_list.extend([moo.btn_event(mp.page_uuid, mp.update2_btn)])
        for message in message_list:
            await websocket.send(json.dumps(message))
            await asyncio.sleep(1)
        await websocket.close()
        time_stamp = int(time.time())
        if moo.isSucess("cloud_save", time_stamp, "after"):
            return True
        else:
            return False


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


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(module_eventa_cfunc_test))
    runner.run(suite)