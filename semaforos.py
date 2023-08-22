from threading import Thread, Semaphore
from time import sleep
import random

def configuracion(id:str):
    print(f"->Sensor {id} configurado.....")

def lectura(id:str):
    print(f"Leyendo datos del sensor {id}")
    return random.randint(0,1000)

def procesamiento(id:str, medicion:float):
    print(f"Se está procesando los datos del sensor {id} con medicion {medicion}")
    sleep(2)
    print(f"Se terminó el procesamiento del sensor {id}")

def cierre(id:str):
    print(f"Se cierra la comunicación del sensor {id}")

# Tarea para los hilos de los sensores
def tarea_sensor(id:str, mediciones:int, tiempo:int, semaforo:Semaphore):
    configuracion(id)
    for _ in range(mediciones):
        medicion = lectura(id)
        with semaforo:
            procesamiento(id, medicion)
        sleep(tiempo)
    cierre(id)

semaforo = Semaphore(5)
n_sensores = 15
n_mediciones = 100
tiempo = 10

for sensor in range(n_sensores):
    hilo = Thread(target=tarea_sensor, args=(str(sensor),n_mediciones, tiempo, semaforo), name=f"sensor" )
    hilo.start()
    


