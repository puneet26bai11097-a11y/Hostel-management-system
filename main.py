from resident_manager import ResidentManager
from room_manager import RoomManager
from billing_manager import BillingManager

def main():
    print("=" * 60)
    print("      WELCOME TO HOSTELOS - SMART MANAGEMENT SYSTEM      ")
    print("=" * 60)

    # Clean up test files if any exist
    res_mgr = ResidentManager("app_residents.json")
    room_mgr = RoomManager("app_rooms.json")
    bill_mgr = BillingManager("app_invoices.json")

    # Step 1: Add Rooms
    print("\n[1] Initializing Room Inventory...")
    room1 = room_mgr.add_room("101-A", "Single", capacity=1, base_rent=5000.0)
    room2 = room_mgr.add_room("102-B", "Double", capacity=2, base_rent=3500.0)
    print(f"Added Room 101-A (Capacity: {room1.capacity}, Rent: ${room1.base_rent})")
    print(f"Added Room 102-B (Capacity: {room2.capacity}, Rent: ${room2.base_rent})")

    # Step 2: Register Resident
    print("\n[2] Registering New Resident...")
    res = res_mgr.register_resident("RES-001", "Alex Mercer", "alex@example.com", "9876543210")
    print(f"Registered: {res.name} (ID: {res.resident_id})")

    # Step 3: Allocate Room
    print("\n[3] Allocating Room 101-A to Resident RES-001...")
    room_mgr.allocate_resident("101-A", res.resident_id)
    res_mgr.update_resident_room(res.resident_id, "101-A")
    print(f"Resident {res.name} assigned to Room {res.room_assigned}")

    # Step 4: Billing Generation
    print("\n[4] Generating Monthly Rent Invoice...")
    assigned_room = room_mgr.get_room(res.room_assigned)
    inv = bill_mgr.create_invoice("INV-1001", res.resident_id, assigned_room.base_rent, utility_charge=450.0)
    print(f"Invoice {inv.invoice_id} created for Resident {res.resident_id}. Total: ${inv.amount_due}")

    # Step 5: Process Payment
    print("\n[5] Processing Payment...")
    bill_mgr.process_payment("INV-1001")
    print(f"Invoice {inv.invoice_id} status updated to: {inv.status}")

    print("\n" + "=" * 60)
    print("          SYSTEM EXECUTION COMPLETED SUCCESSFULLY         ")
    print("=" * 60)

if __name__ == "__main__":
    main()