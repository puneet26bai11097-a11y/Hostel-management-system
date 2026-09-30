# HostelOS: Smart Hostel & Space Allocation System

HostelOS is a modular Python-based management suite designed to handle resident lifecycle management, room inventory allocations, and automated billing generation. Built purely using fundamental Python concepts (OOP, File I/O, Data Structures, Exception Handling), it requires no third-party database drivers.

## Features

* **Module 1: Resident Management**
  * Register, update, search, and check out residents.
  * Validation for email addresses, phone numbers, and unique identification IDs.
* **Module 2: Room Inventory Management**
  * Track room capacities, occupancy levels, and availability states.
  * Dynamically allocate and deallocate residents to specific rooms based on capacity rules.
* **Module 3: Billing & Finance Management**
  * Calculate monthly rent and variable utility surcharges dynamically.
  * Generate itemized billing receipts and process pending payments.

## System Architecture & Workflow

### Process Workflow
1. **Hostel Admin** registers a new resident into the system via `ResidentManager`.
2. Admin checks room availability using `RoomManager` and assigns an available room to the resident.
3. `BillingManager` automatically generates a monthly invoice based on room type and utility usage.
4. Resident makes a payment, and `BillingManager` issues a zero-balance clearance receipt.

### Text-Based UML Diagrams

#### Use Case Diagram
```text
+-------------------------------------------------------------+
|                      HostelOS System                        |
|                                                             |
|   [Admin] ------> (Register / Manage Residents)              |
|   [Admin] ------> (Allocate / Vacate Hostel Rooms)           |
|   [Admin] ------> (Generate Monthly Invoices & Process Rent) |
|                                                             |
+-------------------------------------------------------------+