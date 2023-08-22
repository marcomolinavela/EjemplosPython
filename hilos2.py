from threading import Thread
import time

def tarea1(id, r):
    for i in range(50):
        print(str(id)+":"+str(i)+"->Se ejecuta tarea1..")
        time.sleep(1)

def tarea2(id, r):
    for i in range(50,0,-1):
        print(str(id)+":"+str(i)+"->Se ejecuta el tarea2..")
        time.sleep(0.5)

hilo1 = Thread(target=tarea1, args=(1, 20))
hilo2 = Thread(target=tarea2, args=(2, 20))

hilo1.start()  
hilo2.start() 

hilo1.join()  
hilo2.join()

