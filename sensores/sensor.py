import threading
import random
import time
from database.mongo import MongoDB

class SensorThread(threading.Thread):
    def __init__(self, nome_sensor, intervalo):
        threading.Thread.__init__(self)
        self.nome_sensor = nome_sensor
        self.intervalo = intervalo
        self.sensor_alarmado = False
        self.db = MongoDB()
        self.temperaturas = []

    def run(self):
        while not self.sensor_alarmado:
            temperatura = random.uniform(30, 40)
            self.temperaturas.append(temperatura)
            if len(self.temperaturas) > 60:
                self.temperaturas.pop(0)
            print(f"{self.nome_sensor}: {temperatura} °C")
            if temperatura > 38:
                self.sensor_alarmado = True
                print(f"Atenção! Temperatura muito alta! Verificar Sensor {self.nome_sensor}!")
            self.db.atualizar_sensor(self.nome_sensor, temperatura, self.sensor_alarmado)
            time.sleep(self.intervalo)
