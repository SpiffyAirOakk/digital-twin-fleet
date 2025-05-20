from flask import Flask, render_template
import threading
import json
import paho.mqtt.client as mqtt

app = Flask(__name__)
fleet_data = {}

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe("fleet/data")

def on_message(client, userdata, msg):
    global fleet_data
    fleet_data = json.loads(msg.payload.decode())

def mqtt_loop():
    mqttc = mqtt.Client()
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.connect("localhost", 1883, 60)
    mqttc.loop_forever()

threading.Thread(target=mqtt_loop).start()

@app.route('/')
def index():
    return render_template('dashboard.html', fleet=fleet_data)

if __name__ == '__main__':
    app.run(debug=True)
