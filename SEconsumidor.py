from paho.mqtt import client as cliente_mqtt
import time

broker = '127.0.0.1'
puerto = 1883
tema = "Practica/Test"

cliente = cliente_mqtt.Client()

def conectado(cliente, datos, flags, rc):
    print("Consumidor")
    if rc == 0:
        print("Conectado")
    else:
        print("Fallo en la conexión, ", rc)

cliente.on_connect = conectado
cliente.connect(broker,puerto)

cliente.subscribe(tema)

def mensaje(cliente, datos, msg):
    print(msg.payload.decode())

cliente.on_message = mensaje

cliente.loop_forever()

