import asyncio
import time

async def start_strongman(name, power):
    for i in range (5):
        await asyncio.sleep (10 - power)
        print (f'Силач {name} поднял шар N {i+1}')
    print (f'Силач {name} закончил соревнование')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Nick', 3))
    task_2 = asyncio.create_task(start_strongman('Furry', 7))
    task_3 = asyncio.create_task(start_strongman('Levi', 5))
    await task_1, task_2, task_3

asyncio.run(start_tournament())

 