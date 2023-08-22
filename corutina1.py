import asyncio

async def corutina():
    print("Hola mundo")
    await asyncio.sleep(1)
    print("Hola de nuevo")

asyncio.run(corutina())

