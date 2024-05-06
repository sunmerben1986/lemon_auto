import json
import time
import unittest
from tools.websocket_utils import connect
from page.base_utils import base_utils as bu
from page.page_conf import module_event_after as mp, fe_module_eventa as fmp
from tools.database import db, record


class module_eventa_test(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.moo = bu()
        if not hasattr(type(self), '_is_setup'):
            type(self)._is_setup = True
            self.websocket = await connect()
            message_list = []
            self.timestamp = int(time.time())
            type(self)._timestamp = self.timestamp
            message_list.extend([self.moo.create_page(mp.page_uuid), 
                                 self.moo.base_event(mp.data_list, "event_inited"),
                                 "create_inline",
                                 "validate_inline",
                                 "cancel_inline",
                                 self.moo.page_nation(mp.data_list),
                                 "create_inline",
                                 "save_inline",
                                 self.moo.page_nation(mp.data_list)
                                 ])
            pk = self.moo.get_pk("list")
            message_list.append(self.moo.delete_event_confirm(mp.data_list, pk))
            message_list.append(self.moo.base_event(mp.data_list, "event_delete"))
            for message in message_list:
                print(message)
                await self.websocket.send(json.dumps(message))
                if not hasattr(type(self), '_is_created'):
                    while True:
                        response = await self.websocket.recv()
                        res = self.moo.handle_message(response)
                        if res is None:
                            break
                        elif res == 200:
                            pass
                        elif res != 200 and len(res) == 32:            
                            inline_create = self.moo.create_inline(mp.data_list, res)
                            inline_data = self.moo.set_inline_data(self.timestamp, [mp.text1, mp.text2])
                            inline_data = self.moo.add_inline_data(mp.data_list, res, inline_data)
                            message_list[2] = inline_create
                            message_list[3] = self.moo.validate_event(res, mp.text1, self.timestamp)
                            message_list[4] = self.moo.base_event(res, "event_cancel")
                            message_list[6] = inline_create
                            message_list[7] = inline_data
                            type(self)._is_created = True
                            break
                        else:
                            break
            await self.websocket.close()


    #模型创建事件，创建后触发
    async def test_inline_sm(self):
        response = self.moo.isSucess("create", type(self)._timestamp)
        print(f"test_inline_sm:{response}, {type(self)._timestamp}")
        self.assertIsNotNone(response)
        
    #模型保存事件，保存后触发
    async def test_inline_sm_add(self):
        response = self.moo.isSucess("normal_save", type(self)._timestamp)
        print(f"test_inline_sm_add:{response}, {type(self)._timestamp}")
        self.assertIsNotNone(response)
        
    #模型删除事件，删除后触发
    async def test_delete_inline_data(self):
        response = self.moo.isSucess("normal_delete", type(self)._timestamp)
        print(f"test_delete_inline_data:{response}, {type(self)._timestamp}")
        self.assertIsNotNone(response)
        
    #模型取消事件，取消前触发
    async def test_cancel_inline_data(self):
        respose = self.moo.isSucess("cancel", type(self)._timestamp)
        print(f"test_cancel_inline_data:{respose}, {type(self)._timestamp}")
        self.assertIsNotNone(respose)



if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(module_eventa_test))
    # suite.addTest(module_eventa_test("test_inline_sm_add"))
    runner.run(suite)