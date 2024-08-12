import json
import time
import requests
import unittest
import logging
from const import apijson_const, error_Code
from parameterized import parameterized

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class apijsonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.time_stamp = int(time.time())
        cls.m_name = apijson_const.m_name
        cls.r_name = apijson_const.r_name
        cls.url = apijson_const.url
        cls.post_url = apijson_const.post_url
        cls.put_url = apijson_const.put_url
        cls.get_url = apijson_const.get_url
        cls.querystring = apijson_const.querystring
        cls.data = apijson_const.data
        cls.token = cls.get_token()
        cls.header = {"Authorization": f"Bearer {cls.token}",
                "content-type": "application/json"}

    @classmethod
    def tearDownClass(cls):
        pass
    
    @classmethod
    def get_token(cls):
        response = requests.request("POST", url=cls.url, data=json.dumps(cls.data))
        res = json.loads(response.text)
        data = res.get("data", None)
        access_token = data.get("access_token") if data else None
        return access_token

    def test_insert_data(self): 
        data = apijson_const().set_insert_data(self.time_stamp)
        response = requests.post(url=self.post_url, headers=self.header, data=json.dumps(data), params=self.querystring)
        res = json.loads(response.text)
        self.assertEqual(res.get("code"), 200, error_Code.INSERT_ERROR)
        self.assertTrue(self.is_success(f"{self.time_stamp}", self.r_name), error_Code.INSERT_ERROR)
    
    def test_update_data(self):
        res = self.query_data(self.time_stamp, self.m_name)
        id = res.get(self.m_name, None).get("id", None) if res.get(self.m_name, {}) else None
        self.assertIsNotNone(id, error_Code.UPDATE_ERROR)
        data = apijson_const().set_update_data(id)
        response = requests.post(url=self.put_url, headers=self.header, data=json.dumps(data), params=self.querystring)
        res = json.loads(response.text)
        self.assertEqual(res.get("code"), 200, error_Code.UPDATE_ERROR)
        self.assertTrue(self.is_success(f"{self.time_stamp}", self.r_name), error_Code.UPDATE_ERROR)

    def query_data(self, querystring, dbname):
        data = apijson_const().set_query_data(querystring, dbname)
        response = requests.post(url=self.get_url, headers=self.header, data=json.dumps(data), params=self.querystring)
        res = json.loads(response.text)
        return res

    def is_success(self, querystring, dbname):
        res = self.query_data(querystring, dbname)
        return res.get("code") == 200


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(apijsonTest))
    runner.run(suite)