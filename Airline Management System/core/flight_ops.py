from core.database import read_json, write_json

FLIGHT_PATH = "data/flights/flights.json"

def load_flights():
    data = read_json(FLIGHT_PATH)
    if isinstance(data, dict):  # Fix if file accidentally has a dict
        return [data]
    return data

def add_flight(flight):
    flights = load_flights()
    flights.append(flight)
    write_json(FLIGHT_PATH, flights)

def remove_flight(flight_id):
    flights = load_flights()
    flights = [f for f in flights if f.get('id') != flight_id]
    write_json(FLIGHT_PATH, flights)
