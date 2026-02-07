from sensors.temperateur_sensor import temperature
import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime, timezone



client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    data = {
        "sensor_id": "1",
        "sensor_type": "temperature",
        "value": temperature.read_value(),
        "unite": "C",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    client.publish("home/living_room/temperature", json.dumps(data))
    time.sleep(1)