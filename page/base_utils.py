import json
import random
from tools.database import db, record, module_eventa_tmp, module_eventb_tmp

class base_utils(object):
    event_inited = "9ceef9dcd6da11ea8a7f84c5a603df26"
    event_init_only = "36a408f2565f11eba91984c5a603df26"
    event_result = "9b155308564211eba91984c5a603df26"
    event_sort = "9ceefb08d6da11ea8a7f84c5a603df26"
    event_search = "9ceefc2ad6da11ea8a7f84c5a603df26"
    event_search_save = "8f0c67aa3b595bfcb2bb3c5dd8235d61"
    event_search_select = "749383b6dcae11eaac8184c5a603df26"
    event_dropdown = "168d9cb4e81311ea8af584c5a603df26"
    event_pagination = "9ceefd56d6da11ea8a7f84c5a603df26"
    event_groupby = "ef970066469811ebb00484c5a603df26"
    event_filter = "561c2c1448ea11eb8c6584c5a603df26"
    event_delete = "9cef00e4d6da11ea8a7f84c5a603df26"
    event_inline = "a62c193b7c9b5ef0aaa3b97a5204fa64"
    event_inline_save = "24f35cb716aa5045a7d17048e65eb11c"
    event_export = "482eb0ba8d4355038141170583949a98"
    event_import = "43785ee55f2155559e9731d35abf7cd6"
    event_submit = "2913729aecfb11ea993f84c5a603df26"
    event_delete_confirm = "9110a71f970a58fcab4937f21efdd706"
    event_cascade_delete = "73da3fb8b0515956a731d6219fd7d587"
    event_scan_select = "e9fd75cea3535abf93fc8d328f91fd36"
    event_scan_check = "3634e908b5ac573daaf548fd111a4e65"
    event_external_input = "87ddc8440378534884831c6d9e488696"
    event_selected = "59d8940f65fb595ebf39332bc6ed85f4"
    event_refresh = "1b6cc4125baf566fb7a585d03b3702eb"
    event_validate = "572cfd2ee16e11ea8aef84c5a603df26"
    event_edit = "56b41daae16e11ea8aef84c5a603df26"
    event_cancel = "cc435df5e40e51b086afc4d212a5c197"

    def create_page(self, page_uuid, context={}):
        data = {
            "command":"create_page",
            "data":{
                "page":page_uuid,
                "context":context
                }
            }
        return data
    
    def validate_event(self, component_uuid, filed_uuid, value):
        data = {
            "command":"component_event",
            "data":{
                "component":component_uuid,
                "event":self.event_validate,
                "params":{
                    "field":filed_uuid,
                    "value":value
                    }
                }
            }
        return data

    def page_nation(self, component_uuid):
        data = {
            "command":"component_event",
            "data":{
                "component":component_uuid,
                "event":self.event_pagination,
                "params":{
                    "page_number":1
                    }
                }
            }
        return data

    def create_inline(self, component_uuid, inline_uuid):
        data = {
            "command":"component_event",
            "data":{
                "component":component_uuid,
                "event":self.event_inline,
                "params":{"inline_sm":inline_uuid}
                }
            }
        return data

    def add_inline_data(self, component_uuid, inline_uuid, inline_data={}):
        data = {
            "command":"component_event",
            "data":{
                "component":component_uuid,
                "event":self.event_inline_save,
                "params":{
                    "inline_row_data":{
                        inline_uuid:inline_data
                        }
                    }
                }
        }
        return data

    def exit_page(self, page_uuid):
        data = {
            "command":"exit_page",
            "data":{"page":page_uuid}
            }
        return data
    
    def refresh_page(self, component_uuid):
        data = {
            "command":"component_event",
            "data":{
                "component":component_uuid,
                "event":self.event_refresh,
                "params":{
                    "refresh_args":{
                        "device_type":0,
                        "refresh_type":0
                        }
                    }
                }
            }
        return data
    
    def delete_event_confirm(self, componenet_uuid, pk_list=[]):
        data = {
            "command":"component_event",
            "data":{
                "component":componenet_uuid,
                "event":self.event_delete_confirm,
                "params":{
                    "pk_list":pk_list
                    }
                }
            }
        return data
    
    def refresh_event(self, page_uuid, device_type=0):
        data = {
            "command":"component_event",
            "data":{
                "component":page_uuid,
                "event":self.event_refresh,
                "params":{
                    "refresh_args":{"device_type":device_type}
                    }
                }
            }
        return data
    
    def base_event(self, component_uuid, event):
        if event == "event_edit":
            event_data = self.event_edit
        elif event == "event_cancel":
            event_data = self.event_cancel
        elif event == "event_delete":
            event_data = self.event_delete
        elif event == "event_inited":
            event_data = self.event_inited
        data = {
            "command":"component_event",
            "data":{
                "component":component_uuid,
                "event":event_data,
                "params":{}
                }
            }
        return data
    
    def edit_event(self, page_uuid, component_uuid, context={}):
        data = {
            "command":"create_page",
            "data":{
                "page":page_uuid,
                "parent_machine_id":component_uuid,
                "context":context
                }
            }
        return data
    
    def btn_event(self, page_uuid, component_uuid):
        data = {
            "command":"component_command",
            "data":{
                "component":page_uuid,
                "command":"event",
                "request_id":"3dfd0e27322651ca9c8b58ca39034e1f",
                "params":{
                    "control_uuid":component_uuid
                    },
                "index":0,
                "handle":"click"
                }
            }
        return data
    
    def handle_message(self, message):
        message = json.loads(message)
        result = message.get("result")
        if result == 'on_open':
            return message.get("code")
        elif result == "create_page":
            return message.get("code")
        elif result == "component_event":
            v1 = message.get("data")["values"][0]
            v2 = v1.get("value")
            inline_list = v2.get("forms", [])
            if len(inline_list) != 0:
                return inline_list[0]
    
    def set_inline_data(self, time_stamp, field_uuid_list):
        digits = "0123456789"
        ascii_letters = "abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        str_list = [random.choice(digits +ascii_letters) for i in range(5)]
        random_str = ''.join(str_list)
        inline_data = {field_uuid_list[0]:time_stamp, field_uuid_list[1]:random_str}
        return inline_data

    def get_pk(self, res_type, call_at):
        db.connect()
        if call_at == "before":
            pks = module_eventb_tmp.select(module_eventb_tmp.id)
        elif call_at == "after":
            pks = module_eventa_tmp.select(module_eventa_tmp.id)
        db.close()
        if res_type == "list":
            pk_list = []
            for pk in pks:
                pk_list.append(pk.id)
            return pk_list
        elif res_type == "dict":
            pk_dict = {"pk": list(pks)[0].id}
            return pk_dict
    
    def isSucess(self,tag,item,call_at):
        print(db.close())
        db.connect()
        if tag == "create" or tag == "normal_delete":
            record_data = record.select().where(((record.编号 > item - 30) & (record.编号 < item + 30)), 
                                                record.记录 == tag, record.前后 == call_at).first()
        elif tag == "normal_save" or tag == "cancel":
            record_data = record.select().where(record.编号 == item, record.记录 == tag, record.前后 == call_at).first()
        else:
            record_data = None
        db.close()
        return record_data

if __name__ == "__main__":
    bu = base_utils()
    print(bu.get_pk("list", "after"))