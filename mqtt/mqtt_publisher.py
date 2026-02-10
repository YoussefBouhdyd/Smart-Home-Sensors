from sensors.temperateur_sensor import temperature
from sensors.humidity_sensor import humidity
from sensors.gaz_sensor import gaz
import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime, timezone

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    kitchen_data = {
        "_id": "65f1a2c9e8b4a123456789ab",
        "roomId": "cuisine",
        "tempCapteur": temperature.read_value(),
        "temperaturePrefere": 24,
        "humiditeCapteur": humidity.read_value(),
        "light": True, # We need Sensor for the Light
        "portCapteur": False, # We need Sensor for the Door
        "gazCapteur": gaz.read_value(),
        "climatiseur": True, # We need Sensor for Climatiseur
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    
    client.publish("home/living_room/temperature", json.dumps(temperature_data))

    humidity_data = {
        "sensor_id": "2",
        "sensor_type": "humidity",
        "value": humidity.read_value(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    client.publish("home/living_room/temperature", json.dumps(temperature_data))
    client.publish("home/living_room/humidity", json.dumps(humidity_data))

    time.sleep(5)