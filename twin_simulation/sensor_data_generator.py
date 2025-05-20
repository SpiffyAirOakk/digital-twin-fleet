import random

def generate_mock_data():
    return {
        'speed': round(random.uniform(30, 100), 2),
        'battery': round(random.uniform(20, 100), 2),
        'location': (
            round(random.uniform(-90, 90), 5),
            round(random.uniform(-180, 180), 5)
        )
    }
