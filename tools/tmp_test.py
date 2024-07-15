import json
 

json_data = str({"key1": "value1", 123: "value2"})  # 这里的123是非字符串键
json_data = json.dumps(json_data)
decoded_data = json.loads(json_data)