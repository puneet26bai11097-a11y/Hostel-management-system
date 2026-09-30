import json
import os
from src.models import Invoice

class BillingManager:
    def __init__(self, storage_file: str = "invoices.json"):
        self.storage_file = storage_file
        self.invoices = {}
        self.load_data()

    def create_invoice(self, invoice_id: str, resident_id: str, base_rent: float, utility_charge: float = 0.0) -> Invoice:
        if invoice_id in self.invoices:
            raise ValueError(f"Invoice ID {invoice_id} already exists.")
        total_amount = base_rent + utility_charge
        invoice = Invoice(invoice_id, resident_id, total_amount)
        self.invoices[invoice_id] = invoice
        self.save_data()
        return invoice

    def process_payment(self, invoice_id: str) -> bool:
        if invoice_id not in self.invoices:
            raise KeyError(f"Invoice {invoice_id} not found.")
        invoice = self.invoices[invoice_id]
        if invoice.status == "PAID":
            raise ValueError(f"Invoice {invoice_id} is already paid.")
        
        invoice.status = "PAID"
        self.save_data()
        return True

    def get_invoice(self, invoice_id: str) -> Invoice:
        if invoice_id not in self.invoices:
            raise KeyError(f"Invoice {invoice_id} not found.")
        return self.invoices[invoice_id]

    def save_data(self):
        data = {i_id: obj.to_dict() for i_id, obj in self.invoices.items()}
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    data = json.load(f)
                    self.invoices = {i_id: Invoice.from_dict(obj) for i_id, obj in data.items()}
            except Exception:
                self.invoices = {}