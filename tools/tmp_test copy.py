# import hashlib

# resource_id = hashlib.md5(
#                 "_".join(["80f6b56fa69a53b096e46198ca962418", "c3dcefd65f185c458bb863c37e3b0116", "新建物料档案"]).encode()).hexdigest()
# print(resource_id)
import re


def check_document_name(name: str):
    if len(name) > 40:
        return False
    match_compile = re.compile(r"^(?!\.)[\w\-_\.,@#%^+=\u4E00-\u9FFF]{1,40}")
    return match_lemon_name(match_compile, name)

def match_lemon_name(compile: re.compile, name: str):
    match_obj = compile.match(name)
    if match_obj is None:
        return False
    match_name = match_obj.group()
    if match_name != name:
        return False
    return match_name
print(check_document_name("新建物料档案"))