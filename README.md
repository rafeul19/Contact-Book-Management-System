# Contact Book Management System

A simple, modular Python CLI application to manage your contacts.

---

## Features

- **Add Contact:** Enter name, phone, email, and address. Prevents duplicate phone numbers.
- **View Contacts:** Lists all contacts in a neat, user-friendly format.
- **Search Contact:** Search by name, email, or phone (partial matches allowed).
- **Remove Contact:** Delete a contact by phone number.
- **Persistent Storage:** All data is saved in `contacts.csv`.
- **Input Validation:** Ensures correct data types and formats.
- **No External Libraries:** Uses only Python’s standard library.

---

## Project Structure

```
Contact-Book-Management-System/
│
├── app.py           # Main CLI application
├── address_book.py  # AddressBook class for managing contacts
├── person.py        # Person class (contact data model)
├── helpers.py       # Input validation helpers
├── contacts.csv     # Data file (auto-created)
└── README.md        # Documentation
```

---

## How to Run

1. Make sure you have Python 3 installed.
2. Place all `.py` files in the same directory.
3. Open a terminal in that directory.
4. Run:
   ```bash
   python3 app.py
   ```
5. Follow the on-screen menu.

---

## Sample Usage

```
=========== MENU ===========
1. Add Contact
2. View Contacts
3. Search Contact
4. Remove Contact
5. Exit
============================

Enter your choice: 2

===== All Contacts =====
1. Name : Alice Smith
   Phone : 01711223344
   Email : alice@example.com
   Address: 12/A Lake View, Dhaka

2. Name : Bob
   Phone : 01812345678
   Email : bob@example.com
   Address: 7 Green Street, Chittagong

========================
```

---

## Code Overview

### person.py

- Defines the `Person` class for storing contact details.
- Includes methods for converting to/from dictionaries for CSV operations.

### address_book.py

- Manages the list of contacts.
- Handles loading from and saving to the CSV file.
- Provides methods to add, remove, search, and retrieve all contacts.

### helpers.py

- Contains input validation functions for name, phone, email, and address.

### app.py

- Main entry point.
- Presents the menu and handles user interaction.
- Calls functions from other modules to perform actions.

---

## Notes

- All data is stored in `contacts.csv` in the project directory.
- The application prevents duplicate phone numbers.
- Input is validated for correctness and user-friendly error messages are shown.

---

**This project is fully modular, well-commented, and easy to extend.  
Feel free to use and modify as needed!**
