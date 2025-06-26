from address_book import AddressBook   # Import AddressBook class
from person import Person              # Import Person class
import helpers                         # Import helper functions

# Main function to run the CLI application
def main():
    print("Welcome to the Contact Book CLI System!")         # Welcome message
    book = AddressBook()                                     # Create AddressBook instance
    print(f"Loading contacts from {book.filename}... Done!") # Notify user of loading

    while True:                                              # Start menu loop
        print("""
=========== MENU ===========
1. Add Contact
2. View Contacts
3. Search Contact
4. Remove Contact
5. Exit
============================
""")
        choice = input("Enter your choice: ").strip()        # Get user menu choice

        if choice == "1":                                    # Add Contact option
            while True:
                name = helpers.input_name("Enter Name: ")    # Get and validate name
                if name is not None:
                    break
            while True:
                phone = helpers.input_phone("Enter Phone Number: ") # Get and validate phone
                if phone is not None:
                    break
            while True:
                email = helpers.input_email("Enter Email: ") # Get and validate email
                if email is not None:
                    break
            while True:
                address = helpers.input_address("Enter Address: ") # Get and validate address
                if address is not None:
                    break
            contact = Person(name, phone, email, address)    # Create new Person object
            if book.add_contact(contact):                    # Try to add contact
                print("Contact added successfully!")         # Success message
            else:
                print("Error: Phone number already exists for another contact.") # Duplicate error

        elif choice == "2":                                  # View Contacts option
            book.load_contacts()                             # Reload contacts from CSV
            contacts = book.get_all_contacts()               # Get all contacts
            print("===== All Contacts =====")
            if not contacts:                                 # If no contacts
                print("No contacts found.")                  # Inform user
            else:
                for i, c in enumerate(contacts, 1):          # Enumerate contacts
                    print(f"{i}. Name : {c.name}")           # Print name
                    print(f"   Phone : {c.phone}")           # Print phone
                    print(f"   Email : {c.email}")           # Print email
                    print(f"   Address: {c.address}\n")      # Print address
            print("========================")

        elif choice == "3":                                  # Search Contact option
            term = input("Enter search term (name/email/phone): ").strip() # Get search term
            results = book.search_contacts(term)             # Search contacts
            if results:                                      # If results found
                print("Search Result:")
                for c in results:
                    print(f"Name : {c.name}")                # Print name
                    print(f"Phone : {c.phone}")              # Print phone
                    print(f"Email : {c.email}")              # Print email
                    print(f"Address: {c.address}\n")         # Print address
            else:
                print("No contact found.")                   # No results message

        elif choice == "4":                                  # Remove Contact option
            phone = input("Enter the phone number of the contact to delete: ").strip() # Get phone
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ").strip() # Confirm
            if confirm.lower() == "y":                       # If confirmed
                if book.remove_contact(phone):               # Try to remove
                    print("Contact deleted successfully!")   # Success message
                else:
                    print("Contact not found.")              # Not found message

        elif choice == "5":                                  # Exit option
            print("Thank you for using the Contact Book CLI System. Goodbye!") # Goodbye message
            break                                            # Exit loop

        else:
            print("Invalid choice. Please try again.")       # Invalid menu choice

# Run the main function if this file is executed
if __name__ == "__main__":
    main()