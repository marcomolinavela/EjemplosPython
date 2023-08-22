from paho.mqtt import client as cliente_mqtt
import time

# broker = '172.24.144.59'
broker = '127.0.0.1'
puerto = 1883
tema = "Practica/Test"

cliente = cliente_mqtt.Client()

def conectado(cliente, datos, flags, rc):
    print("Marco-SE2")
    if rc == 0:
        print("Conectado")
    else:
        print("Fallo en la conexión, ", rc)

cliente.on_connect = conectado
cliente.connect(broker,puerto)
cliente.loop_start()

cliente.publish(tema,"Practica2 SE-2")
cliente.disconnect()
time.sleep(1)