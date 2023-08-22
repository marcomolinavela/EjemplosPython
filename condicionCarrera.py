from threading import Thread, Lock
from time import sleep

def sumador(monto, repeticiones, lock):
    global contador 
    for _ in range(repeticiones):
        with lock:
            tmp = contador
            sleep(0)
            tmp = tmp + monto
            sleep(0)
            contador = tmp

def restador(monto, repeticiones, lock):
    global contador 
    for _ in range(repeticiones):
        with lock:
            tmp = contador
            sleep(0)
            tmp = tmp - monto
            sleep(0)
            contador = tmp

contador = 0
lock = Lock()
hilo_sumador = Thread(target=sumador, args=(100, 1000000, lock))
hilo_restador = Thread(target=restador, args=(100, 1000000, lock))

hilo_sumador.start()  
hilo_restador.start() 
 
hilo_sumador.join()  
hilo_restador.join()
print("El valor de contador es: ", contador)
