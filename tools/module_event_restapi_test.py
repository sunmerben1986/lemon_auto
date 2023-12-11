import asyncio
import json
import sys
import os
import time
import random
import requests


class restapiTest():
    def __init__(self) -> None:
        self.url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/b858071bb83c5aa0bd9a40ce09572d9e/restful/v1/insert'
        self.querystring = {"tenant_uuid": "b858071bb83c5aa0bd9a40ce09572d9e"}
        self.time_stamp = int(time.time())

    def test_insert_data(self): 
        data = {
            "data":[
                {"编号":self.time_stamp,"类型":"restapi insert"}
                ]
                }
        response = requests.post(url=self.url, data=data)
    
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
    aa = restapiTest()
    print(aa.test_insert_data())