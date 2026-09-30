import json
import re
import os
from src.models import Resident

class ResidentManager:
    def __init__(self, storage_file: str = "residents.json"):
        self.storage_file = storage_file
        self.residents = {}
        self.load_data()

    def _validate_email(self, email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    def _validate_phone(self, phone: str) -> bool:
        return phone.isdigit() and len(phone) >= 10

    def register_resident(self, resident_id: str, name: str, email: str, phone: str) -> Resident:
        if resident_id in self.residents:
            raise ValueError(f"Resident with ID {resident_id} already exists.")
        if not self._validate_email(email):
            raise ValueError(f"Invalid email format: {email}")
        if not self._validate_phone(phone):
            raise ValueError(f"Invalid phone number: {phone}. Must be at least 10 digits.")

        resident = Resident(resident_id, name, email, phone)
        self.residents[resident_id] = resident
        self.save_data()
        return resident

    def get_resident(self, resident_id: str) -> Resident:
        if resident_id not in self.residents:
            raise KeyError(f"Resident with ID {resident_id} not found.")
        return self.residents[resident_id]

    def update_resident_room(self, resident_id: str, room_number: str):
        resident = self.get_resident(resident_id)
        resident.room_assigned = room_number
        self.save_data()

    def remove_resident(self, resident_id: str):
        if resident_id in self.residents:
            del self.residents[resident_id]
            self.save_data()
        else:
            raise KeyError(f"Resident ID {resident_id} does not exist.")

    def save_data(self):
        data = {r_id: obj.to_dict() for r_id, obj in self.residents.items()}
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    data = json.load(f)
                    self.residents = {r_id: Resident.from_dict(obj) for r_id, obj in data.items()}
            except Exception:
                self.residents = {}