from threading import Thread
import time

def tarea1(id, r):
    global contador 
    for i in range(50):
        contador += 1
        time.sleep(1)

def tarea2(id, r):
    global contador 
    for i in range(50,0,-1):
        print("->Contador =", contador)
        time.sleep(1)

contador = 0

hilo1 = Thread(target=tarea1, args=(1, 20))
hilo2 = Thread(target=tarea2, args=(2, 20))

hilo1.start()  
hilo2.start() 

hilo1.join()  
hilo2.join()
