import time
import json
import paho.mqtt.client as mqtt
from twin_simulation.fleet_manager import FleetManager

fleet = FleetManager(count=5)
broker = "localhost"
topic = "fleet/data"

client = mqtt.Client()

client.connect(broker, 1883, 60)
client.loop_start()

while True:
    fleet.update_all()
    data = fleet.get_data()
    payload = json.dumps(data)
    client.publish(topic, payload)
    print("Published data:", payload)
    time.sleep(3)
