import unittest
import os
from resident_manager import ResidentManager

class TestResidentManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_residents.json"
        self.manager = ResidentManager(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_register_resident_success(self):
        res = self.manager.register_resident("R101", "John Doe", "john@example.com", "1234567890")
        self.assertEqual(res.name, "John Doe")
        self.assertEqual(self.manager.get_resident("R101").email, "john@example.com")

    def test_invalid_email_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.register_resident("R102", "Jane Doe", "invalid-email", "1234567890")

    def test_invalid_phone_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.register_resident("R103", "Bob", "bob@example.com", "1234")