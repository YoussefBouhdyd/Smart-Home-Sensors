import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print(f"Topic: {msg.topic} | Data: {data}")

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)


client.subscribe("home/+/temperature")    
client.subscribe("home/+/humidity")

client.loop_forever()
