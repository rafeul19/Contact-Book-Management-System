from address_book import AddressBook
from person import Person
import helpers

def main():
    print("Welcome to the Contact Book CLI System!")
    book = AddressBook()
    print(f"Loading contacts from {book.filename}... Done!")

    while True:
        print("""
=========== MENU ===========
1. Add Contact
2. View Contacts
3. Search Contact
4. Remove Contact
5. Exit
============================
""")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            while True:
                name = helpers.input_name("Enter Name: ")
                if name is not None:
                    break
            while True:
                phone = helpers.input_phone("Enter Phone Number: ")
                if phone is not None:
                    break
            while True:
                email = helpers.input_email("Enter Email: ")
                if email is not None:
                    break
            while True:
                address = helpers.input_address("Enter Address: ")
                if address is not None:
                    break
            contact = Person(name, phone, email, address)
            if book.add_contact(contact):
                print("Contact added successfully!")
            else:
                print("Error: Phone number already exists for another contact.")
        elif choice == "2":
            book.load_contacts()  # Reload contacts from CSV every time before viewing
            contacts = book.get_all_contacts()
            print("===== All Contacts =====")
            if not contacts:
                print("No contacts found.")
            else:
                for i, c in enumerate(contacts, 1):
                    print(f"{i}. Name : {c.name}")
                    print(f"   Phone : {c.phone}")
                    print(f"   Email : {c.email}")
                    print(f"   Address: {c.address}\n")
            print("========================")
        elif choice == "3":
            term = input("Enter search term (name/email/phone): ").strip()
            results = book.search_contacts(term)
            if results:
                print("Search Result:")
                for c in results:
                    print(f"Name : {c.name}\nPhone : {c.phone}\nEmail : {c.email}\nAddress: {c.address}\n")
            else:
                print("No contact found.")
        elif choice == "4":
            phone = input("Enter the phone number of the contact to delete: ").strip()
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ").strip()
            if confirm.lower() == "y":
                if book.remove_contact(phone):
                    print("Contact deleted successfully!")
                else:
                    print("Contact not found.")
        elif choice == "5":
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()