# import subprocess
import asyncio
import time

# # async def main():
# #     hilo1 = asyncio.create_task(subprocess.call(['python', 'estrella_Multiple.py']))
# #     await asyncio.gather(hilo1)
# async def tarea1():
#     subprocess.call(['python', 'estrella_Multiple.py'])

# async def tarea2():
#     subprocess.call(['py', 'estrella_3D.py'])

# async def main():
#     task1 = asyncio.create_task(tarea1())
#     task2 = asyncio.create_task(tarea2())
#     await asyncio.gather(task1, task2)

# asyncio.run(main())

async def tarea1():
    process = await asyncio.create_subprocess_exec('py', 'estrella_Multiple.py')
    await process.wait()

async def tarea2():
    process = await asyncio.create_subprocess_exec('py', 'estrella_3D.py')
    await process.wait()

async def main():
    task1 = asyncio.create_task(tarea1())
    task2 = asyncio.create_task(tarea2())
    await asyncio.gather(task1, task2)

asyncio.run(main())