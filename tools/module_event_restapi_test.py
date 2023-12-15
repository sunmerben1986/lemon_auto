import json
import time
import requests


class restapiTest():
    def __init__(self) -> None:
        self.url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/b858071bb83c5aa0bd9a40ce09572d9e/restful/v1/'
        self.querystring = {"tenant_uuid": "b858071bb83c5aa0bd9a40ce09572d9e"}
        self.time_stamp = int(time.time())

    def test_insert_data(self):
        tag = "insert"
        post_url = self.url + tag
        data = {
            "data":{
                "编号":self.time_stamp,"类型":"restapi insert"}
                }
        res = requests.post(url=post_url, data=json.dumps(data))
        if res.json().get("code") == 200:
            assert self.is_success(self.time_stamp)
    
    def test_update_data(self):
        tag = "update"
        post_url = self.url + tag
        data = {
            "data":{
                "target":"1702346338","destination":"restapi update"}
                }
        res = requests.post(url=post_url, data=json.dumps(data))
        if res.json().get("code") == 200:
            assert self.is_success("1702346338")

    def test_delete_data(self):
        tag = "delete"
        post_url = self.url + tag
        data = {
            "data":{
                "target":"1702346338"}
                }
        res = requests.post(url=post_url, data=json.dumps(data))
        if res.json().get("code") == 200:
            if not self.is_success("1702346338"):
                assert True
            else:
                assert False

    def query_data(self, querystring):
        tag = "search"
        post_url = self.url + tag
        data = {
            "data":{"target": querystring}
        }
        res = requests.post(post_url, data=json.dumps(data))
        return res.json()

    def is_success(self, querystring):
        res = self.query_data(querystring)
        if res.get("code") == 200:
            return True
        else:
            return False


if __name__ == "__main__":
    aa = restapiTest()
    print(aa.test_delete_data())