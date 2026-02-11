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

def read_sensor_data(room_name):
    return {
        "roomid": room_name+"-sensor",
        "temperature": temperature.read_value(),
        "humidity": humidity.read_value(),
        "gaz": gaz.read_value(),
    }
def create_room_data(sensor_id, room_name):
    return {
        **read_sensor_data(room_name),
        "motion": {
            "sensor_id": sensor_id,
            "sensor_type": "motion",
            "value": random.choice([True, False]),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    }
rooms = [
    {"id": "001", "name": "living_room"},
    {"id": "002", "name": "kitchen"},
    {"id": "003", "name": "bathroom"}
]
while True:  
    for room in rooms:
        room_data = create_room_data(room["id"], room["name"])
        client.publish(f"home/{room['name']}", json.dumps(room_data))
        time.sleep(1)
