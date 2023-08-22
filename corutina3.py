import asyncio
from time import sleep

async def corutina(tiempo):
    print("Hola mundo")
    await asyncio.sleep(tiempo)
    # sleep(2)
    print("Hola de nuevo")

async def main():
    await asyncio.gather(corutina(2), corutina(2))
    
asyncio.run(main())
