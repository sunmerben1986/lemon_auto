import datetime
import uuid
import json

class Tools:
    def gen_timetostr():
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def gen_uuid():
        return str(uuid.uuid5(uuid.uuid1(), str(uuid.uuid1()))).replace("-", "")

    def _create_invitation_code():
        import random
        import string

        invitation_codes = set()
        chars_hub = string.ascii_letters+string.digits
        strip_words = ['1', 'i', 'l', '0', 'o', 'O', 'I']
        for word in strip_words:
            chars_hub = chars_hub.replace(word, "")
        for _ in range(8):
            invitation_codes.add("".join([random.choice(chars_hub) for i in range(8)]))

        return invitation_codes
    
    def get_inline_uuid(content):

        inline_uuid = json.loads(content).get("data")

        return inline_uuid


if __name__ == "__main__":
    pass