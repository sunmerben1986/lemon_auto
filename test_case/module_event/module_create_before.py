import asyncio
import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from tools.normal_tools import Tools
from tools.send_da import send_data
from page.document_conf import module_event_before as mp
from page.module_obj import Module_obj as mb
from tools.database import db, record



class module_create_before(unittest.TestCase):
    def test_module_create_before(self):
        time_no = Tools.gen_timetostr()
        request_all = []
        mbb = mb()
        request_all.append(mbb.create_page(mp.page_uuid))
        request_all.append(mbb.init_event(mp.data_list))
        request_all.append(mbb.create_inline(mp.data_list, Tools.gen_uuid()))

        asyncio.run(send_data.connect_to_websocket(request_all))

        self.assertTrue(self.isSucess(time_no))

    def isSucess(self, item):
        db.connect()
        record_data = record.select().where(record.编号 == item).first()
        if record_data:
            return True
        else:
            return False

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(module_create_before('test_module_create_before'))
    runner.run(suite)