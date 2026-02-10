from sensors.temperateur_sensor import temperature
from sensors.humidity_sensor import humidity
from sensors.gaz_sensor import gaz
import paho.mqtt.client as mqtt
import json
import time

client = mqtt.Client()
client.connect("localhost", 1883)

while True:  
    client.publish("home/living_room/temperature", json.dumps(temperature.read_value()))
    client.publish("home/kichen/temperature", json.dumps(temperature.read_value()))
    client.publish("home/living_room/humidity", json.dumps(humidity.read_value()))
    client.publish("home/living_room/gaz", json.dumps(gaz.read_value()))
    time.sleep(5)