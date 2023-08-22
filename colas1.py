from threading import Thread
import threading
from queue import Queue
from time import sleep

def extraccion(n, fifo:Queue):
    for i in range(n):
        elemento = fifo.get()
        sleep(2)
        print(f"Hilo {threading.current_thread().name}: Preceó el elemento {elemento}")
        fifo.task_done()


fifo = Queue()
for i in range(12):
    fifo.put(f"item {i}")

hilo1 = Thread(target=extraccion, args=(3, fifo), name="Hilo 1")
hilo2 = Thread(target=extraccion, args=(4, fifo), name="Hilo 2")
hilo3 = Thread(target=extraccion, args=(5, fifo), name="Hilo 3")
hilo1.start()
hilo2.start()
hilo3.start()
fifo.join()

print("Se termina el hilo principal")


