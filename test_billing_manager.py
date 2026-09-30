import unittest
import os
from src.billing_manager import BillingManager

class TestBillingManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_invoices.json"
        self.manager = BillingManager(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_invoice_creation_and_payment(self):
        inv = self.manager.create_invoice("INV01", "RES01", base_rent=1000.0, utility_charge=200.0)
        self.assertEqual(inv.amount_due, 1200.0)
        self.assertEqual(inv.status, "UNPAID")

        self.manager.process_payment("INV01")
        self.assertEqual(self.manager.get_invoice("INV01").status, "PAID")