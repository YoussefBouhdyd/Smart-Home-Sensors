import paho.mqtt.client as mqtt
from datetime import datetime, timezone
import json
# from db_handler import collection

def on_message(client, userdata, msg):
    print(f"TData: {msg.payload.decode()}")
    # collection.insert_one({
    #     **data,
    #     "timestamp": datetime.now(timezone.utc).isoformat()
    # })

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)


client.subscribe("home/living_room")    
# client.subscribe("home/+/+")

client.loop_forever()
