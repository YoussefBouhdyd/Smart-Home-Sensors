from sensors.temperateur_sensor import temperature
from sensors.humidity_sensor import humidity
from sensors.anomalous import anomalous
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
        "temperature": anomalous(temperature.read_value(),60,random.randint(30,40)),
        "humidity": humidity.read_value(),
        "gaz": anomalous(gaz.read_value(),60,random.randint(2000,40000)),
    }
def create_room_data(sensor_id, room_name):
    return {
        **read_sensor_data(room_name),
        "motion": {
            "sensor_id": sensor_id,
            "sensor_type": "motion",
            "value": anomalous(False,60,True),
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
        if not room_data.get("roomid") or room_data.get("temperature") is None:
            print(f"Invalid data for {room['name']}: missing required fields")
            continue
        
        result = client.publish(f"home/{room['name']}", json.dumps(room_data))
        
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"✓ Data sent successfully to home/{room['name']}")
            print(f"  Room: {room_data['roomid']} | Temp: {room_data['temperature']}°C | Humidity: {room_data['humidity']}%")
        else:
            print(f"✗ Failed to send data to home/{room['name']} (code: {result.rc})")
        
        time.sleep(1)
        # try:
        # except Exception as e:
        #     print(f"✗ Error publishing data for {room['name']}: {str(e)}")
        #     time.sleep(1)
