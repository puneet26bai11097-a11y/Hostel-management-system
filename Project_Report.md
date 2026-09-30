# ACADEMIC PROJECT REPORT
## HostelOS: Autonomous Smart Hostel Management System

---

### 1. Cover Page
* **Project Title**: HostelOS - Autonomous Smart Hostel Management System
* **Course**: Computer Science & Software Engineering (Flipped Evaluation)
* **Student Name / ID**: [ PUNEET WADHWANI /  26BAI11097 ]
* **Date**: September 28, 2026

---

### 2. Introduction
HostelOS is a comprehensive Python application designed to streamline daily hostel operations including resident profile management, room allocation based on live capacity constraints, and transparent fee generation.

---

### 3. Problem Statement
Manual hostel administration faces operational issues such as room double-booking, invalid record generation, lack of audit trails, and slow billing processing. `HostelOS` solves these challenges through modular automation.

---

### 4. Functional Requirements
1. **Module 1: Resident Management**: Full CRUD capability, unique ID assignment, and regex validation for contact info.
2. **Module 2: Room Inventory Control**: Dynamic tracking of room states, occupant lists, and strict capacity checks.
3. **Module 3: Billing & Invoicing Engine**: Automated rent computation including utility surcharges and status updates.

---

### 5. Non-Functional Requirements
1. **Reliability**: File-based persistence layer prevents data loss on exit.
2. **Usability**: Clear modular APIs and clean user execution output.
3. **Maintainability**: Strict separation of concerns following Object-Oriented Design principles.
4. **Error Handling**: Custom exception handling for duplicate keys, invalid inputs, and overbooking.

---

### 6. System Architecture
The application employs a 3-Tier Layered Architecture:
* **Presentation/Execution Layer**: `main.py`
* **Business Logic Layer**: `ResidentManager`, `RoomManager`, `BillingManager`
* **Data Access Layer**: JSON File Persistence (`residents.json`, `rooms.json`, `invoices.json`)

---

### 7. Design Diagrams

#### Use Case Diagram
* **Actors**: Warden / Hostel Administrator
* **Actions**: Register Resident, Add Room, Assign Resident to Room, Generate Bill, Process Payment.

#### Workflow Diagram
`Register Resident` -> `Check Room Availability` -> `Assign Bed` -> `Generate Bill` -> `Process Payment`

#### Sequence Diagram
1. User invokes `allocate_resident(room_number, resident_id)`.
2. `RoomManager` checks `room.is_available()`.
3. If True, appends `resident_id` to `occupants` and triggers `save_data()`.

---

### 8. Design Decisions & Rationale
* **Language Choice**: Python 3.10 standard library to keep execution lightweight and zero-dependency.
* **Storage Choice**: Lightweight JSON files for easy portability and direct inspectability without installing complex SQL servers.

---

### 9. Implementation Details
The project consists of 6 standard code files (`models.py`, `resident_manager.py`, `room_manager.py`, `billing_manager.py`, `main.py`, and test classes), meeting the academic criterion of 5-10 structured modules.

---

### 10. Screenshots / Results
*(Upon running `python src/main.py`, the CLI terminal output demonstrates complete end-to-end execution of room addition, resident onboarding, room assignment, invoice generation, and status updating).*

---

### 11. Testing Approach
* **Unit Testing Framework**: Python `unittest`.
* **Scope**: Automated tests cover invalid email format handling, capacity overflow prevention, duplicate ID checks, and payment state transitions.

---

### 12. Challenges Faced
* **Concurrency & Persistence Syncing**: Solved by enforcing atomic file save operations (`save_data()`) after every state mutation.
* **Validation Accuracy**: Enforced via standard Regular Expressions (`re` library).

---

### 13. Learnings & Key Takeaways
* Practical application of Object-Oriented Programming (OOP) concepts: Encapsulation, Abstraction, and Data Hiding.
* Implementing robust testing patterns and file-handling logic in pure Python.

---

### 14. Future Enhancements
* Integration of a Graphical User Interface (GUI) using PyQt or Tkinter.
* Relational database back-end (SQLite/PostgreSQL) for large-scale enterprise scaling.

---

### 15. References
* Python Documentation: https://docs.python.org/3/
* Software Engineering Best Practices for Clean Code & Modular Design.