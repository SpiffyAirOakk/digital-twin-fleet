
# 🚚 Digital Twin Mock for Fleet Management (with Real-time MQTT Integration)

A **Digital Twin** simulation of a vehicle fleet powered by Python, MQTT (Mosquitto), and Flask. This project simulates vehicle telemetry data (OBD-II style), streams it in real time using MQTT, and visualizes it on a live dashboard.

---

## 🌐 Overview

This system represents a **mock digital twin** of a fleet of vehicles, simulating key parameters like speed, battery status, and location. Data is transmitted over an MQTT broker to mimic real-world telemetry streaming from IoT-enabled vehicles.

### ✅ Key Features

- ⚙️ Simulates multiple vehicle states (speed, battery, GPS)
- 📡 Streams data to MQTT topic in real-time
- 🧠 Fleet manager to control and update all vehicles
- 🌍 Flask dashboard that updates dynamically using MQTT
- 🪟 Responsive, auto-refreshing front-end

---

## 📁 Project Structure

```
digital-twin-fleet-mgmt/
├── main.py                        # Entry point for dashboard
├── mqtt_client.py                # Simulates and publishes vehicle data
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
│
├── twin_simulation/              # Core logic for digital twin simulation
│   ├── vehicle.py                # Vehicle class
│   ├── fleet_manager.py          # Fleet management and updates
│   └── sensor_data_generator.py  # Random mock data generator
│
├── dashboard/                    # Web dashboard (Flask app)
│   ├── app.py                    # Flask app with MQTT client
│   └── templates/
│       └── dashboard.html        # HTML dashboard template
│
└── utils/
    └── logger.py (optional)      # Centralized logger utility
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/digital-twin-fleet-mgmt.git
cd digital-twin-fleet-mgmt
```

### 2. Install Python Requirements

```bash
pip install -r requirements.txt
```

### 3. Start MQTT Broker (Mosquitto)

> Make sure Mosquitto is installed and running on port `1883`.

- **Linux/macOS**:
  ```bash
  sudo systemctl start mosquitto
  ```
- **Windows**:
  Run `mosquitto.exe` from the install folder or start the Mosquitto service.

---

## 🚀 Running the Project

### 🛰️ 1. Start the MQTT Publisher

```bash
python mqtt_client.py
```

This script:
- Simulates OBD-II data for multiple vehicles
- Publishes real-time data to MQTT topic `fleet/data`

### 🖥️ 2. Launch the Flask Dashboard

```bash
python main.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🧠 Code Breakdown

### `vehicle.py`

Defines the structure of a vehicle:

```python
class Vehicle:
    def __init__(self, vehicle_id):
        self.speed = 0
        self.battery = 100
        self.location = (0.0, 0.0)
```

---

### `sensor_data_generator.py`

Generates random telemetry data (simulating sensors):

```python
def generate_mock_data():
    return {
        'speed': round(random.uniform(30, 100), 2),
        'battery': round(random.uniform(20, 100), 2),
        'location': (
            round(random.uniform(-90, 90), 5),
            round(random.uniform(-180, 180), 5)
        )
    }
```

---

### `fleet_manager.py`

Manages all vehicles in the fleet:

```python
class FleetManager:
    def update_all(self):
        for vehicle in self.vehicles.values():
            vehicle.update_state(generate_mock_data())
```

---

### `mqtt_client.py`

Publishes fleet data to MQTT:

```python
while True:
    fleet.update_all()
    data = fleet.get_data()
    client.publish("fleet/data", json.dumps(data))
    time.sleep(3)
```

---

### `dashboard/app.py`

Subscribes to `fleet/data`, parses the real-time MQTT data, and renders the dashboard.

```python
@app.route('/')
def index():
    return render_template('dashboard.html', fleet=fleet_data)
```

---

### `dashboard.html`

Live-updating front-end using meta-refresh:

```html
<meta http-equiv="refresh" content="5">
```

---

## 🧪 Test with MQTT CLI Tools

Use Mosquitto CLI tools to test:

```bash
# Subscriber (view data)
mosquitto_sub -h localhost -t fleet/data

# Publisher (send manual command)
mosquitto_pub -h localhost -t fleet/command -m "restart"
```

---

## 📦 Future Improvements

- Replace polling with WebSocket + MQTT bridge
- Add map visualization with Leaflet.js
- Store historical data in a time-series DB (e.g., InfluxDB)
- Add login/authentication for fleet control

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License

MIT License. See `LICENSE` file.

---

## 🧑‍💻 Author

Abdullah Khalid
Machine Learning Engineer | CV2X & Smart Mobility Enthusiast
