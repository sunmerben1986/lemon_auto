"""
一些用于apijson测试的常量
"""

class apijson_const:
        r_name = "事件记录"
        m_name = "模型事件测试事件前"
        # querystring = {"tenant_uuid": "b858071bb83c5aa0bd9a40ce09572d9e"}
        querystring = {"tenant_uuid": "4824f3abed4f569380c654e6b6ab537e"}
        url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/auth/login.json'
        post_url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/apijson/v1/post'
        put_url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/apijson/v1/put'
        get_url = 'https://tlemon.lemonstudio.tech:8443/8f646bbd87e25fecb72e128eb4f98c49test/api/apijson/v1/get'
        # data = {
        #     "login_type": 5,
        #     "app_key": "ajMWBCAFCCFECIGJCBCA",
        #     "app_secret": "E4KoksXCs31NiyEjFdPz9VlPkD3Y83UV"
        # }
        data = {
            "login_type": 5,
            "app_key": "LiJxAHBFBIFDEEFHHDGD",
            "app_secret": "KK4iWJEbPYwkm8kwswisUtK47q0EdzK5"
        }

        def set_insert_data(self, time_stamp):
            api_data = {
                "模型事件测试事件前": [
                    {
                        "编号": "",
                        "备注": "apijson插入"
                    }
                ],
                "tag": "模型事件测试事件前"
            } 
            api_data["模型事件测试事件前"][0]["编号"] = time_stamp
            return api_data

        def set_update_data(self, id):
            update_data = {
                    "模型事件测试事件前":{
                            "id": "",
                            "备注": "apijson更新"
                        },
                    "tag": "模型事件测试事件前"
            }
            update_data["模型事件测试事件前"]["id"] = id
            return update_data

        def set_query_data(self, querystring, dbname):
            query_data = {
                dbname: {
                    "编号": querystring,
                    "@column": "id,编号"
                    }
            }
            return query_data


class error_Code:
        INSERT_ERROR = "插入数据失败"
        UPDATE_ERROR = "更新数据失败"
        QUERY_ERROR = "查询数据失败"