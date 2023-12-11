import asyncio
import json
import sys
import os
import time
import random
import requests


class apijsonTest():
    def __init__(self) -> None:
        self.url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/auth/login.json'
        self.post_url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/apijson/v1/post'
        self.put_url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/apijson/v1/put'
        self.get_url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/apijson/v1/get'
        self.data = {
            "login_type": 5,
            "app_key": "ajMWBCAFCCFECIGJCBCA",
            "app_secret": "yCIqBRJQxk7LMuReCteQjJhOxWQF9bVo"
        }
        self.token = self.get_token()
        self.querystring = {"tenant_uuid": "b858071bb83c5aa0bd9a40ce09572d9e"}
        self.header = {"Authorization": f"Bearer {self.token}",
                "content-type": "application/json"}
        self.time_stamp = int(time.time())

    def get_token(self):
        response = requests.post(url=self.url, data=json.dumps(self.data))
        res = json.loads(response.text)
        data = res.get("data")
        access_token = data.get("access_token")
        return access_token

    def test_insert_data(self): 
        data = {
            "模型事件测试事件前": [
                {
                    "编号": self.time_stamp,
                    "备注": "apijson插入"
                }
            ],
            "tag": "模型事件测试事件前"
        }
        response = requests.post(url=self.post_url, headers=self.header, data=json.dumps(data), params=self.querystring)
        res = json.loads(response.text)
        if res.get("code") == 200:
            assert self.is_success(f"{self.time_stamp}", "事件记录")
    
    def test_update_data(self):
        res = self.query_data("1701855919", "模型事件测试事件前")
        id = res.get("模型事件测试事件前", {}).get("id")
        data = {
            "模型事件测试事件前":{
                    "id": id,
                    "记录": "apijson更新"
                },
            "tag": "模型事件测试事件前"
        }
        response = requests.post(url=self.put_url, headers=self.header, data=json.dumps(data), params=self.querystring)
        res = json.loads(response.text)
        if res.get("code") == 200:
            assert self.is_success(f"1701855919", "事件记录")

    def query_data(self, querystring, dbname):
        data = {
        dbname: {
            "编号": querystring,
            "@column": "id,编号"
            }
        }
        response = requests.post(url=self.get_url, headers=self.header, data=json.dumps(data), params=self.querystring)
        res = json.loads(response.text)
        return res

    def is_success(self, querystring, dbname):
        res = self.query_data(querystring, dbname)
        if res.get("code") == 200:
            return True
        else:
            return False


if __name__ == "__main__":
    aa = apijsonTest()
    print(aa.test_update_data())