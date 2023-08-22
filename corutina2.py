import asyncio
from time import sleep

async def corutina():
    print("Hola mundo")
    await asyncio.sleep(2)
    # sleep(2)
    print("Hola de nuevo")

async def main():
    tarea1 = asyncio.create_task(corutina())
    tarea2 = asyncio.create_task(corutina())
    await tarea1
    await tarea2

asyncio.run(main())

