# import requests
# import zipfile

# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

# url = "https://img2.baidu.com/it/u=2080244369,3435160753&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500"

# resp = requests.get(url, headers=header)

# with open("C:\\1_日常工作\\4_code\Personal\\tools\\test_ima.jpg", 'wb') as f:
#     f.write(resp.content)

# url = "https://lemon-resources-production.oss-cn-shenzhen.aliyuncs.com/runtime/dbc0d924e9cd5522a666ce0622acf825test/e2ebefea4573513d9fa0ff9ead834f72/c8c9d84dd32e5c8b96fcbd3ecc51408a/cf0c89165755563ea549940d6c6a161b/254015ded9b05a9d893f97cc3089e932/0e63f3f0faed50b78c116749d4cfefdb/%E8%A3%85%E4%BF%AE%E6%B8%85%E5%8D%95.xlsx?OSSAccessKeyId=LTAI5tMNPLXwZdVWUkLqb8UB&Expires=2008736692&Signature=pfTByL6HOURM3%2FdkaKvBeX5FpRk%3D"

# resp = requests.get(url)

# with open("C:\\1_日常工作\\4_code\Personal\\tools\\test_xlsx.xlsx", 'wb') as f:
#      f.write(resp.content)