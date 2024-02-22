import asyncio

async def func1():
    print("我是func1")
    await asyncio.sleep(3)
    print("func1结束")

async def func2():
    print("我是func2")
    await asyncio.sleep(2)
    print("func2结束")

async def func3():
    print("我是func3")
    await asyncio.sleep(1)
    print("func3结束")


# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1,f2,f3]
#     asyncio.run(asyncio.wait(tasks))

# def test():
#     return True, {}
# a, b = test()
# print(a, b)

# list_dict = {'1天':1,'2天':2,'3天':3,'5天':5,'6天':6}
# for k, v in list_dict.items():
#     print(k, v)

# 工作流任务数量 = (
#     工作流任务模型
#     .select(peewee.fn.Count(peewee.SQL('1')).alias('count'))
#     .join(系统用户表模型, on=(工作流任务模型.处理人 == 系统用户表模型.唯一标识符))
#     .join(工作流节点模型, on=(工作流任务模型.所属节点 == 工作流节点模型.节点标识符))
#     .join(工作流实例模型, on=(工作流节点模型.工作流 == 工作流实例模型.工作流标识符))
#     .where(((工作流实例模型.名称.contains(工作流名称)) | (工作流实例模型.名称.contains(附加工作流名称))) & (工作流节点模型.节点状态 == 0) & (系统用户表模型.唯一标识符 == lemon.system.current_user.uuid) & (工作流实例模型.运行状态 == 0) & (工作流任务模型.创建任务时间 >= 1683129600))
#     .scalar()
# )
a = [1,2,3,4]
for item in a:
    print(item)
    a.remove(item)
    print(a)