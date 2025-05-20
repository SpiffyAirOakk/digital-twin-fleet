class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.speed = 0
        self.battery = 100
        self.location = (0.0, 0.0)

    def update_state(self, data):
        self.speed = data.get('speed', self.speed)
        self.battery = data.get('battery', self.battery)
        self.location = data.get('location', self.location)

    def to_dict(self):
        return {
            'vehicle_id': self.vehicle_id,
            'speed': self.speed,
            'battery': self.battery,
            'location': self.location
        }
