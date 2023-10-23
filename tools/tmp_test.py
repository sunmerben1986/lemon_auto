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


if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [f1,f2,f3]
    asyncio.run(asyncio.wait(tasks))