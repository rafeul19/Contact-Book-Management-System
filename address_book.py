import csv                # Import csv module for reading/writing CSV files
from person import Person # Import the Person class

# Define the AddressBook class to manage a list of contacts
class AddressBook:
    # Initialize AddressBook with a filename for storage
    def __init__(self, filename="contacts.csv"):
        self.filename = filename   # Store the filename for CSV storage
        self.contacts = []         # Initialize an empty list for contacts
        self.load_contacts()       # Load contacts from the CSV file

    # Load contacts from the CSV file into the contacts list
    def load_contacts(self):
        try:
            with open(self.filename, newline='', encoding='utf-8') as f: # Open CSV file
                reader = csv.DictReader(f)                               # Create a CSV reader
                self.contacts = [Person.from_dict(row) for row in reader]# Convert each row to a Person
        except FileNotFoundError:
            self.contacts = []      # If file doesn't exist, start with empty list

    # Save all contacts to the CSV file
    def save_contacts(self):
        with open(self.filename, 'w', newline='', encoding='utf-8') as f: # Open CSV file for writing
            fieldnames = ["name", "phone", "email", "address"]            # Define CSV headers
            writer = csv.DictWriter(f, fieldnames=fieldnames)             # Create a CSV writer
            writer.writeheader()                                          # Write headers
            for contact in self.contacts:
                writer.writerow(contact.to_dict())                        # Write each contact as a row

    # Add a new contact if phone number is unique
    def add_contact(self, contact):
        if any(c.phone == contact.phone for c in self.contacts): # Check for duplicate phone
            return False                                         # Return False if duplicate
        self.contacts.append(contact)                            # Add contact to list
        self.save_contacts()                                     # Save updated list to file
        return True                                              # Return True if added

    # Remove a contact by phone number
    def remove_contact(self, phone):
        for i, c in enumerate(self.contacts):    # Loop through contacts
            if c.phone == phone:                 # If phone matches
                del self.contacts[i]             # Delete the contact
                self.save_contacts()             # Save updated list
                return True                      # Return True if deleted
        return False                             # Return False if not found

    # Search contacts by term (case-insensitive, partial match)
    def search_contacts(self, term):
        term = term.lower()                      # Convert search term to lowercase
        return [
            c for c in self.contacts
            if term in c.name.lower() or         # Match in name
               term in c.email.lower() or        # Match in email
               term in c.phone                   # Match in phone
        ]

    # Return all contacts
    def get_all_contacts(self):
        return self.contacts                     # Return the list of contacts