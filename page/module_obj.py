import json

class Module_obj:
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

    def create_page(self, page_uuid, context={}):
        data = {
            "command":"create_page",
            "data":{
                "page":page_uuid,
                "context":context
                }
            }
        return data
    
    def validate_event(self, component_uuid, filed_uuid):
        data = {
            "command":"component_event",
            "data":{
                "component":component_uuid,
                "event":self.event_validate,
                "params":{
                    "field":filed_uuid,
                    "value":""
                    }
                }
            }
        return data
    
    def init_event(self, component_uuid):
        data = {
            "command":"component_event",
            "data":{
                "component":component_uuid,
                "event":self.event_inited,
                "params":{}
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

    def delete_event(self, component_uuid):
        data = {
            "command":"component_event",
            "data":{
                "component":component_uuid,
                "event":self.event_delete,
                "params":{}
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
    
    def any_event(self, component_uuid, event):
        if event == "event_edit":
            event_data = self.event_edit
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

if __name__ == "__main__":
    pass