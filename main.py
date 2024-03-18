from sensores.sensor import SensorThread
import threading
import time

# Criar Threads para os sensores
threads = [
    SensorThread("Temp1", 5),
    SensorThread("Temp2", 3),
    SensorThread("Temp3", 7)
]

# Iniciar as Threads dos sensores
for thread in threads:
    thread.start()

# Esperar pelas Threads dos sensores terminarem
for thread in threads:
    thread.join()
