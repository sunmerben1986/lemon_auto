import json
 

json_data = str({"key1": "value1", 123: "value2"})  # 这里的123是非字符串键
json_data = json.dumps(json_data)
decoded_data = json.loads(json_data)
# 计算两个日期的间隔函数
# 2018-01-01 2018-01-02
# 1
# 2018-01-01 2018-01-01
# 0
# 2018-01-01 2017-12-31
# -1
# 2018-01-01 2017-12-30

# import random

# random.choice()
# for item in range(2):
#     print(2)

# def f():
#     pass
# code = f.__code__
# print(code.co_code)
# print(code.co_stacksize)
# print(dir(code))

# from abc import ABCMeta, abstractmethod
# class builder(classmethod=ABCMeta):
#     @abstractmethod
#     def create_page(self, page_uuid):
#         pass
# from runtime import Args
# from typings._get_data._get_data import Input, Output
from decimal import Decimal
import requests

"""
Each file needs to export a function named `handler`. This function is the entrance to the Tool.

Parameters:
args: parameters of the entry function.
args.input - input parameters, you can get test input value by args.input.xxx.
args.logger - logger instance used to print logs, injected by runtime.

Remember to fill in input/output in Metadata, it helps LLM to recognize and use tool.

Return:
The return data of the function, which should match the declared output parameters.
"""
# from bs4 import BeautifulSoup
# def handler():

#     url = "http://zen.lemonstudio.tech:9000/zentao/user-login-f82p6ubo9krvo8005v2dc78gq6.json"

#     querystring = {"account":"zhou.bin","password":"zbfight@321"}
#     payload = "-----011000010111000001101001--\r\n\r\n"
#     headers = {"content-type": "multipart/form-data; boundary=---011000010111000001101001"}
#     response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
#     cookies = response.cookies
#     url = "http://zen.lemonstudio.tech:9000/zentao/bug-browse-1-0-bySearch-myQueryID--154-150-1.html"
#     querystring = {"zentaosid":cookies.get("zentaosid")}
#     payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"zentaosid\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
#     headers = {"content-type": "multipart/form-data; boundary=---011000010111000001101001"}
#     response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
#     bs = BeautifulSoup(response.text,"html.parser")
#     print(bs)
#     bugs = bs.select("tbody")[0].select("tr")
#     all_bugs = []
#     for bug in bugs:
#         bug_id = bug.find_all("a")[0].text
#         summary = bug.find_all("td")[3].text
#         creater = bug.find_all("td")[6].text
#         assignto = bug.find_all("td")[8].text
#         item = {"缺陷编号":bug_id, "缺陷标题":summary, "提交者":creater, "指派给":assignto}
#         all_bugs.append(item)
#         print(all_bugs)

# handler()
# if 0 is not None:
#     print("ok")
#     print(Decimal(0))
#     if Decimal(1):
#         value = 0
#         print(value)
# else:
#     print("no")
import json
with open("D:\\3_Python\\4.txt", "r",encoding="utf-8") as f:
    res = json.loads(f.read())
    data = res.get("data").get("data")
    count = 0
    for item in data:
        tmp = len(item.get("search_res"))
        count += tmp
    print(count)