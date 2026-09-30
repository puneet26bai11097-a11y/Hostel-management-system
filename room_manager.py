import json
import os
from src.models import Room

class RoomManager:
    def __init__(self, storage_file: str = "rooms.json"):
        self.storage_file = storage_file
        self.rooms = {}
        self.load_data()

    def add_room(self, room_number: str, room_type: str, capacity: int, base_rent: float) -> Room:
        if room_number in self.rooms:
            raise ValueError(f"Room {room_number} already exists.")
        room = Room(room_number, room_type, capacity, base_rent)
        self.rooms[room_number] = room
        self.save_data()
        return room

    def allocate_resident(self, room_number: str, resident_id: str):
        if room_number not in self.rooms:
            raise KeyError(f"Room {room_number} does not exist.")
        room = self.rooms[room_number]
        if not room.is_available():
            raise ValueError(f"Room {room_number} is already at full capacity.")
        if resident_id in room.occupants:
            raise ValueError(f"Resident {resident_id} is already in Room {room_number}.")
        
        room.occupants.append(resident_id)
        self.save_data()

    def deallocate_resident(self, room_number: str, resident_id: str):
        if room_number not in self.rooms:
            raise KeyError(f"Room {room_number} does not exist.")
        room = self.rooms[room_number]
        if resident_id not in room.occupants:
            raise ValueError(f"Resident {resident_id} not found in Room {room_number}.")
        
        room.occupants.remove(resident_id)
        self.save_data()

    def get_room(self, room_number: str) -> Room:
        if room_number not in self.rooms:
            raise KeyError(f"Room {room_number} not found.")
        return self.rooms[room_number]

    def save_data(self):
        data = {r_num: obj.to_dict() for r_num, obj in self.rooms.items()}
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    data = json.load(f)
                    self.rooms = {r_num: Room.from_dict(obj) for r_num, obj in data.items()}
            except Exception:
                self.rooms = {}