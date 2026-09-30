import unittest
import os
from src.room_manager import RoomManager

class TestRoomManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_rooms.json"
        self.manager = RoomManager(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_and_allocate_room(self):
        room = self.manager.add_room("101", "Single", capacity=1, base_rent=500.0)
        self.assertTrue(room.is_available())
        
        self.manager.allocate_resident("101", "RES1")
        self.assertFalse(self.manager.get_room("101").is_available())

    def test_overcapacity_allocation_raises_error(self):
        self.manager.add_room("102", "Single", capacity=1, base_rent=500.0)
        self.manager.allocate_resident("102", "RES1")
        with self.assertRaises(ValueError):
            self.manager.allocate_resident("102", "RES2")