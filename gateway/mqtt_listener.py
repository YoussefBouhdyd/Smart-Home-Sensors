import paho.mqtt.client as mqtt
from datetime import datetime, timezone
import json

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    kitchen_data = {
        "id": "cuisine",
        "tempCapteur": msg.payload,
        "temperaturePrefere": 24 ,
        "humiditeCapteur": msg.payload,
        "light": True, # We need Sensor for the Light
        "portCapteur": False, # We need Sensor for the Door
        "gazCapteur": msg.pay,
        "climatiseur": True, # We need Sensor for Climatiseur
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
#   "_id": {
#     "$oid": "69890c4cbbca503dcd4497ab"
#   },
#   "id": "livingroom",
#   "tempCapteur": 22.1,
#   "humiditeCapteur": 54,
#   "light": false,
#   "doorCapteur": true,
#   "gazCapteur": null,
#   "climatiseur": true,
#   "temperaturePrefere": 22,
#   "timestamp": "2026-02-08T23:21:00.966672"
# }
    # livingroom_data = {
    #     "roomId": "livingroom",
    #     "tempCapteur": temperature.read_value(),
    #     "temperaturePrefere": 24,
    #     "humiditeCapteur": humidity.read_value(),
    #     "light": True, # We need Sensor for the Light
    #     "portCapteur": False, # We need Sensor for the Door
    #     "gazCapteur": gaz.read_value(),
    #     "climatiseur": True, # We need Sensor for Climatiseur
    #     "timestamp": datetime.now(timezone.utc).isoformat()
    # }
    # toilet_data = {
    #     "roomId": "toilet",
    #     "tempCapteur": temperature.read_value(),
    #     "temperaturePrefere": 24,
    #     "humiditeCapteur": humidity.read_value(),
    #     "light": True, # We need Sensor for the Light
    #     "portCapteur": False, # We need Sensor for the Door
    #     "gazCapteur": gaz.read_value(),
    #     "climatiseur": True, # We need Sensor for Climatiseur
    #     "timestamp": datetime.now(timezone.utc).isoformat()
    # }
    # bedroom_data = {
    #     "roomId": "bedroom",
    #     "tempCapteur": temperature.read_value(),
    #     "temperaturePrefere": 24,
    #     "humiditeCapteur": humidity.read_value(),
    #     "light": True, # We need Sensor for the Light
    #     "portCapteur": False, # We need Sensor for the Door
    #     "gazCapteur": gaz.read_value(),
    #     "climatiseur": True, # We need Sensor for Climatiseur
    #     "timestamp": datetime.now(timezone.utc).isoformat()
    # }
    # print(f"Topic: {msg.topic} | Data: {data}")
    # print(dir(msg))

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)

# kitchen_data = {
#         "roomId": "cuisine",
#         "tempCapteur": temperature.read_value(),
#         "temperaturePrefere": 24,
#         "humiditeCapteur": humidity.read_value(),
#         "light": True, # We need Sensor for the Light
#         "portCapteur": False, # We need Sensor for the Door
#         "gazCapteur": gaz.read_value(),
#         "climatiseur": True, # We need Sensor for Climatiseur
#         "timestamp": datetime.now(timezone.utc).isoformat()
# }

# humidity_data = {
#     "sensor_id": "2",
#     "sensor_type": "humidity",
#     "value": humidity.read_value(),
#     "timestamp": datetime.now(timezone.utc).isoformat()
# }

client.subscribe("home/+/temperature")    
client.subscribe("home/+/humidity")

client.loop_forever()
