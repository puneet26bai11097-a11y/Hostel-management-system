import json

class Resident:
    def __init__(self, resident_id: str, name: str, email: str, phone: str, room_assigned: str = None):
        self.resident_id = resident_id
        self.name = name
        self.email = email
        self.phone = phone
        self.room_assigned = room_assigned

    def to_dict(self):
        return {
            "resident_id": self.resident_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "room_assigned": self.room_assigned
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            resident_id=data["resident_id"],
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            room_assigned=data.get("room_assigned")
        )


class Room:
    def __init__(self, room_number: str, room_type: str, capacity: int, base_rent: float):
        self.room_number = room_number
        self.room_type = room_type  # e.g., "Single", "Double", "Suite"
        self.capacity = capacity
        self.base_rent = base_rent
        self.occupants = []  # List of resident_ids

    def is_available(self) -> bool:
        return len(self.occupants) < self.capacity

    def to_dict(self):
        return {
            "room_number": self.room_number,
            "room_type": self.room_type,
            "capacity": self.capacity,
            "base_rent": self.base_rent,
            "occupants": self.occupants
        }

    @classmethod
    def from_dict(cls, data: dict):
        room = cls(
            room_number=data["room_number"],
            room_type=data["room_type"],
            capacity=data["capacity"],
            base_rent=data["base_rent"]
        )
        room.occupants = data.get("occupants", [])
        return room


class Invoice:
    def __init__(self, invoice_id: str, resident_id: str, amount_due: float, status: str = "UNPAID"):
        self.invoice_id = invoice_id
        self.resident_id = resident_id
        self.amount_due = amount_due
        self.status = status  # "UNPAID", "PAID"

    def to_dict(self):
        return {
            "invoice_id": self.invoice_id,
            "resident_id": self.resident_id,
            "amount_due": self.amount_due,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            invoice_id=data["invoice_id"],
            resident_id=data["resident_id"],
            amount_due=data["amount_due"],
            status=data["status"]
        )