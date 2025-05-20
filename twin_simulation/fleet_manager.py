from twin_simulation.vehicle import Vehicle
from twin_simulation.sensor_data_generator import generate_mock_data

class FleetManager:
    def __init__(self, count=5):
        self.vehicles = {f'VEH-{i}': Vehicle(f'VEH-{i}') for i in range(1, count+1)}

    def update_all(self):
        for vehicle in self.vehicles.values():
            vehicle.update_state(generate_mock_data())

    def get_data(self):
        return {vid: v.to_dict() for vid, v in self.vehicles.items()}
