import paho.mqtt.client as mqtt
from datetime import datetime, timezone
import json
from db_handler import collection

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    collection.insert_one({
        **data,
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

    # kitchen_data = {
    #     "id": "cuisine",
    #     "tempCapteur": msg.payload,
    #     "temperaturePrefere": 24 ,
    #     "humiditeCapteur": msg.payload,
    #     "light": True, # We need Sensor for the Light
    #     "portCapteur": False, # We need Sensor for the Door
    #     "gazCapteur": msg.pay,
    #     "climatiseur": True, # We need Sensor for Climatiseur
    #     "timestamp": datetime.now(timezone.utc).isoformat()
    # }

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)


client.subscribe("home/+/+")    
client.subscribe("home/+/+")

client.loop_forever()
