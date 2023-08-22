from threading import Thread
import time

def hilo(id, r):
    for i in range(10):
        print(str(id)+":"+str(i)+"-->Se ejecuta el hilo..")
        time.sleep(1)
    
obj_hilo = Thread(target=hilo, args=(1, 10))
obj_hilo.start()  # inicia el hilo

obj_hilo2 = Thread(target=hilo, args=(2, 10))
obj_hilo2.start()  # inicia el hilo

obj_hilo3 = Thread(target=hilo, args=(3, 10))
obj_hilo3.start()  # inicia el hilo

obj_hilo.join()   # Espera la ejecucion del hilo
obj_hilo2.join()   # Espera la ejecucion del hilo
obj_hilo3.join()   # Espera la ejecucion del hilo
