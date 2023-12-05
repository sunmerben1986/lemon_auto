import asyncio
import json
import sys
import os
import time
import random
import requests


class apijsonTest():
    def __init__(self) -> None:
        self.url = 'https://tlemon.lemonstudio.tech:8443/6ccc8e92c5045c6bbf1f04c3339c0010test/api/auth/login.json'
        self.data = {
            "login_type": 5,
            "app_key": "ajMWBCAFCCFECIGJCBCA",
            "app_secret": "yCIqBRJQxk7LMuReCteQjJhOxWQF9bVo"
        }

    def get_token(self):
        response = requests.post(url=self.url, data=json.dumps(self.data))
        res = json.loads(response.text)
        data = res.get("data")
        access_token = data.get("access_token")
        return access_token

    def test_insert_data(self):
        header = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3V1aWQiOiI1MWRiNWE4Nzg0YzA\
                1ZmQwYjY0NGQ0NzA3M2Q2MTFkYSIsImV4cCI6MTczMzQxMTIwNn0.DNMMEkawZ1Uzo0W1iUJYqgNvCviz8heoTgJlBLv1-Ug"}
        data = {
            "模型事件测试事件前": [
                {
                    "编号": "202306271448",
                    "备注": "apijson插入"
                }
            ],
            "tag": "模型事件测试事件前"
        }
        res = requests.post(url=self.url, headers=header, data=json.dumps(data))
        print(res)

if __name__ == "__main__":
    aa = apijsonTest()
    print(aa.test_insert_data())