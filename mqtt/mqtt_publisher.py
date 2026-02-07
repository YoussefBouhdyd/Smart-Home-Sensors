from sensors.temperateur_sensor import temperature
from sensors.humidity_sensor import humidity
import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime, timezone

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    temperature_data = {
        "sensor_id": "1",
        "sensor_type": "temperature",
        "value": temperature.read_value(),
        "unite": "C",
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