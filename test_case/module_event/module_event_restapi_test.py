import json
import time
import requests
import unittest


class restapiTest(unittest.TestCase):
    url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/b858071bb83c5aa0bd9a40ce09572d9e/restful/v1/'
    querystring = {"tenant_uuid": "b858071bb83c5aa0bd9a40ce09572d9e"}
    time_stamp = int(time.time())
    auth = ("周斌".encode("utf-8"), "zbfight@321")
    header = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3V1aWQiOiI1MWRiNWE4Nzg0YzA1ZmQwYjY0NGQ0NzA3M2Q2MTFkYSIsImV4cCI6MTczNjE0MjA4OH0.831Pfrd4dKuYsIS5hAIOQLY_XldORH4TIB5YI3t0kDk"}
        
    #柠檬鉴权添加数据
    def test_insert_lm(self):
        tag = "/lm/insert"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp,"类型":"token"}
                }
        res = requests.post(url=post_url, data=json.dumps(data), headers=self.header)
        if res.json().get("code") == 200:
            assert self.is_success(tag="/lm/search",auth="token",data=data)

    #匿名添加数据
    def test_insert_am(self):
        tag = "/am/insert"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp,"类型":"anymous"}
                }
        res = requests.post(url=post_url, data=json.dumps(data))
        if res.json().get("code") == 200:
            assert self.is_success(tag="/am/search",auth="anymous",data=data)
    
    #basic添加数据
    def test_insert_ba(self):
        tag = "/ba/insert"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp,"类型":"Basic"}
                }
        res = requests.post(url=post_url, data=json.dumps(data), auth=("周斌".encode("utf-8"), "zbfight@321"))
        if res.json().get("code") == 200:
            assert self.is_success(tag="/ba/search",auth="Basic",data=data)
    
    #柠檬鉴权更新数据
    def test_update_lm(self):
        tag = "/lm/update"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp,"类型":"token", "destination":"lm_update"}
                }
        res = requests.put(url=post_url, data=json.dumps(data), headers=self.header)
        if res.json().get("code") == 200:
            data["data"]["类型"] = data["data"]["destination"]
            assert self.is_success(tag="/lm/search",auth="token",data=data)
    
    #匿名更新数据
    def test_update_am(self):
        tag = "/am/update"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp,"类型":"anymous", "destination":"am_update"}
                }
        res = requests.put(url=post_url, data=json.dumps(data))
        if res.json().get("code") == 200:
            data["data"]["类型"] = data["data"]["destination"]
            assert self.is_success(tag="/am/search",auth="anymous",data=data)
    
    #basic更新数据
    def test_update_ba(self):
        tag = "/ba/update"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp,"类型":"Basic", "destination":"ba_update"}
                }
        res = requests.put(url=post_url, data=json.dumps(data), auth=("周斌".encode("utf-8"), "zbfight@321"))
        if res.json().get("code") == 200:
            data["data"]["类型"] = data["data"]["destination"]
            assert self.is_success(tag="/ba/search",auth="Basic",data=data)

    #柠檬鉴权删除数据
    def test_xdelete_lm(self):
        tag = "/lm/delete"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp, "类型":"lm_update"}
                }
        res = requests.delete(url=post_url, data=json.dumps(data), headers=self.header)
        if res.json().get("code") == 200:
            if not self.is_success(tag="/lm/search",auth="token",data=data):
                assert True
            else:
                assert False
    
    #匿名删除数据
    def test_xdelete_am(self):
        tag = "/am/delete"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp, "类型":"am_update"}
                }
        res = requests.delete(url=post_url, data=json.dumps(data))
        if res.json().get("code") == 200:
            if not self.is_success(tag="/am/search",auth="anymous",data=data):
                assert True
            else:
                assert False

    #basic删除数据
    def test_xdelete_ba(self):
        tag = "/ba/delete"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp, "类型":"ba_update"}
                }
        res = requests.delete(url=post_url, data=json.dumps(data), auth=("周斌".encode("utf-8"), "zbfight@321"))
        if res.json().get("code") == 200:
            if not self.is_success(tag="/ba/search",auth="Basic",data=data):
                assert True
            else:
                assert False

    def is_success(self, **querystring):
        tag = querystring.get("tag")
        auth = querystring.get("auth", None)
        data = querystring.get("data")
        post_url = self.url + tag
        if auth == "anymous":
            res = requests.get(post_url, data=json.dumps(data))
        elif auth == "Basic":
            res = requests.get(post_url, data=json.dumps(data), auth=self.auth)
        elif auth == "token":
            res = requests.get(post_url, data=json.dumps(data), headers=self.header)
        else:
            res = None
        if res.json().get("code") == 200:
            return True
        else:
            return False


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(restapiTest))
    runner.run(suite)