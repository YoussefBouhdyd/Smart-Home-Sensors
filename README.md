# Smart-Home-Sensors
This repository contains the sensor layer of a Smart Home IoT system. Its main purpose is to simulate or interface with home sensors, collect environmental and device data, and store it in a database for consumption by other system components.
# Files Structures
```
repo/
│
├── sensors/
│   ├── temperature_sensor.py
│   ├── humidity_sensor.py
│   ├── motion_sensor.py
│
├── mqtt/
│   ├── mqtt_publisher.py
│
├── coap/
│   ├── coap_server.py
│
├── gateway/
│   ├── mqtt_listener.py
│   ├── coap_client.py
│   ├── db_handler.py
│
├── config/
│   ├── settings.yaml
│
└── README.md
```

# How To Run
Install all dependicies

```
pip install -r requirements.txt
```

```
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```