from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.bancoiot
        self.sensores_collection = self.db.sensores

    def atualizar_sensor(self, nome_sensor, temperatura, sensor_alarmado):
        sensor_data = {
            'nomeSensor': nome_sensor,
            'valorSensor': temperatura,
            'unidadeMedida': 'C°',
            'sensorAlarmado': sensor_alarmado
        }
        self.sensores_collection.update_one({'nomeSensor': nome_sensor}, {'$set': sensor_data}, upsert=True)
