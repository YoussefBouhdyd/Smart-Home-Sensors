import json
import time
import random
from datetime import datetime, timezone

import paho.mqtt.client as mqtt


BROKER_HOST = "localhost"
BROKER_PORT = 1883

MOTION_TOPIC = "home/living_room/motion"
MOTION_SENSOR_ID = "3"


def read_motion() -> bool:
    """
    Simulate a motion sensor.

    Returns True if motion is detected, False otherwise.
    Currently implemented as a random boolean with a bias
    towards 'no motion' to feel more realistic.
    """
    # ~25% chance of detecting motion
    return random.random() < 0.25


def main() -> None:
    client = mqtt.Client()
    client.connect(BROKER_HOST, BROKER_PORT)

    # while True:
    motion_detected = read_motion()

    motion_data = {
        "sensor_id": MOTION_SENSOR_ID,
        "sensor_type": "motion",
        "value": motion_detected,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    client.publish(MOTION_TOPIC, json.dumps(motion_data))

    # Adjust the interval as needed; 5 seconds matches the other sensors.
    time.sleep(5)


if __name__ == "__main__":
    main()