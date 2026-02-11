from sensors.temperateur_sensor import temperature
from sensors.humidity_sensor import humidity
from sensors.gaz_sensor import gaz
import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime, timezone

client = mqtt.Client()
client.connect("localhost", 1883)

while True:  
    
    data = {
        "temperature": temperature.read_value(),
        "humidity": humidity.read_value(),
        "gaz": gaz.read_value(),
        "motion": {
            "sensor_id": "003",
            "sensor_type": "motion",
            "value": random.choice([True, False]),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    }
    client.publish("home/living_room", json.dumps(data))

    
    # client.publish("home/living_room/temperature", json.dumps(temperature.read_value()))
    # client.publish("home/living_room/humidity", json.dumps(humidity.read_value()))
    # client.publish("home/living_room/gaz", json.dumps(gaz.read_value()))
