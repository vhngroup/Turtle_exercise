import asyncio
import time

async def EstrellaMultiple():
    process = await asyncio.create_subprocess_exec('py', 'estrella_Multiple.py')
    await process.wait()

async def Estrella3D():
    process = await asyncio.create_subprocess_exec('py', 'estrella_3D.py')
    await process.wait()

async def main():
    task1 = asyncio.create_task(EstrellaMultiple())
    task2 = asyncio.create_task(Estrella3D())
    await asyncio.gather(task1, task2)

asyncio.run(main())