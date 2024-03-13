import asyncio
import json
import sys
import os
import time
import random
import unittest
from tools.websocket_utils import connect
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
print(sys.path)
from page.module_obj import Module_obj as mo
from page.document_conf import module_event_after as mp
from page.document_conf import fe_module_eventa as fmp
from tools.database import db, record, module_eventa_tmp



class module_eventa_test(unittest.IsolatedAsyncioTestCase):
#模型创建事件，创建后触发
    async def test_inline_sm(self):
        websocket = await connect()
        message_list = []
        moo = mo()
        message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list)])
        for message in message_list:
            await websocket.send(json.dumps(message))
            while True:
                response = await websocket.recv()
                res = await self.handle_message(response)
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
        response = await self.isSucess("create", int(time.time()))
        if response:
            return True
        else:
            return False
        
    #模型保存事件，保存后触发
    async def test_inline_sm_add(self):
        websocket = await connect()
        message_list = []
        moo = mo()
        message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list)])
        for message in message_list:
            await websocket.send(json.dumps(message))
            while True:
                response = await websocket.recv()
                res = await self.handle_message(response)
                if res is None:
                    break
                elif res != 200 and len(res) == 32:            
                    inline_create = moo.create_inline(mp.data_list, res)
                    inline_data, item = self.set_inline_data(res, [mp.text1, mp.text2])
                    inline_data = moo.add_inline_data(mp.data_list, res, inline_data)
                    message_list.append(inline_create)
                    message_list.append(inline_data)
                elif res == 200:
                    pass
                else:
                    break
        await websocket.close()
        response = await self.isSucess("save", item)
        if response:
            return True
        else:
            return False
        
    #模型删除事件，删除后触发
    async def test_delete_inline_data(self):
        websocket = await connect()
        message_list = []
        moo = mo()
        pk_list = self.get_pk_list()
        message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list), 
                            moo.delete_event_confirm(mp.data_list, pk_list), moo.delete_event(mp.data_list), moo.refresh_event(mp.page_uuid)])
        for message in message_list:
            await websocket.send(json.dumps(message))
        await websocket.close()
        time_stamp = int(time.time())
        response = await self.isSucess("delete", time_stamp)
        if response:
            return True
        else:
            return False
        
    #模型取消事件，取消前触发
    async def test_delete_inline_data(self):
        websocket = await connect()
        message_list = []
        moo = mo()
        pk_dict = self.get_pk_dict()
        message_list.extend([moo.create_page(mp.page_uuid), moo.init_event(mp.data_list), 
                            moo.edit_event(mp.page_uuid, mp.data_list, pk_dict), moo.any_event(fmp.page_uuid, "event_edit"), moo.refresh_event(mp.page_uuid)])
        for message in message_list:
            await websocket.send(json.dumps(message))
        await websocket.close()
        time_stamp = int(time.time())
        response = await self.isSucess("delete", time_stamp)
        if response:
            return True
        else:
            return False

    async def isSucess(self,tag,item):
        db.connect()
        if tag == "create" or tag == "delete":
            record_data = record.select().where(((record.编号 > item - 3) & (record.编号 < item + 3)), 
                                                record.记录 == tag, record.前后 == "after").first()
        elif tag == "save":
            record_data = record.select().where(record.编号 == item, record.记录 == tag, record.前后 == "after").first()
        return record_data

    async def get_pk_list(self):
        db.connect()
        pks = module_eventa_tmp.select(module_eventa_tmp.id)
        pk_list = []
        for pk in pks:
            pk_list.append(pk.id)
        db.close()
        return pk_list

    async def get_pk_dict(self):
        db.connect()
        pk = module_eventa_tmp.select(module_eventa_tmp.id).first()
        pk_dict = {"pk": pk}
        db.close()
        return pk_dict

    async def set_inline_data(self, inline_uuid, field_uuid_list):
        digits = "0123456789"
        ascii_letters = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str_list = [random.choice(digits +ascii_letters) for i in range(5)]
        random_str = ''.join(str_list)
        time_stamp = int(time.time())
        inline_data = {field_uuid_list[0]:time_stamp, field_uuid_list[1]:random_str}
        return inline_data, time_stamp

    async def handle_message(self, message):
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
    suite.addTest(unittest.makeSuite(module_eventa_test))
    runner.run(suite)