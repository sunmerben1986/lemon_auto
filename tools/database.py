from peewee import *

db = MySQLDatabase('t_test_8f646b_b858071', user='b858071bb83c_test_8f646b', password='UEghInx9', host='tlemon.lemonstudio.tech', port=3306)

class record(Model):
    id = IntegerField()
    编号 = CharField()
    记录 = CharField()
    前后 = CharField()

    class Meta:
        database = db
        table_name = '主模块|事件记录'

class module_eventb_tmp(Model):
    id = IntegerField()
    编号 = CharField()
    备注 = CharField()

    class Meta:
        database = db
        table_name = '主模块|模型事件测试事件前'

class module_eventa_tmp(Model):
    id = IntegerField()
    编号 = CharField()
    备注 = CharField()

    class Meta:
        database = db
        table_name = '主模块|模型事件测试事件后'