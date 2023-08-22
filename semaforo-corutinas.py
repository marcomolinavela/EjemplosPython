# from threading import Thread, Semaphore
from asyncio import  Semaphore
import asyncio
from time import sleep
import random

async def configuracion(id:str):
    print(f"->Sensor {id} configurado.....")

async def lectura(id:str):
    print(f"Leyendo datos del sensor {id}")
    return random.randint(0,1000)

async def procesamiento(id:str, medicion:float):
    print(f"Se está procesando los datos del sensor {id} con medicion {medicion}")
    await asyncio.sleep(2)
    print(f"Se terminó el procesamiento del sensor {id}")

async def cierre(id:str):
    print(f"Se cierra la comunicación del sensor {id}")

async def tarea_sensor(id:str, mediciones:int, tiempo:int, semaforo:Semaphore):
    await configuracion(id)
    for _ in range(mediciones):
        medicion = await lectura(id)
        async with semaforo:
            await procesamiento(id, medicion)
        await asyncio.sleep(tiempo)
    await cierre(id)

async def main():
    semaforo = Semaphore(5)
    n_sensores = 15
    n_mediciones = 100
    tiempo = 10
    tareas = []
    for i in range(n_sensores):
        tareas.append(tarea_sensor(str(i), n_mediciones, tiempo, semaforo))
    await asyncio.gather(*tareas)
    
        
asyncio.run(main())


