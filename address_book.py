import csv
from person import Person

class AddressBook:
    def __init__(self, filename="contacts.csv"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.contacts = [Person.from_dict(row) for row in reader]
            print(f"Loaded {len(self.contacts)} contacts.")  # Debug line
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ["name", "phone", "email", "address"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())

    def add_contact(self, contact):
        if any(c.phone == contact.phone for c in self.contacts):
            return False
        self.contacts.append(contact)
        self.save_contacts()
        return True

    def remove_contact(self, phone):
        for i, c in enumerate(self.contacts):
            if c.phone == phone:
                del self.contacts[i]
                self.save_contacts()
                return True
        return False

    def search_contacts(self, term):
        term = term.lower()
        return [
            c for c in self.contacts
            if term in c.name.lower() or term in c.email.lower() or term in c.phone
        ]

    def get_all_contacts(self):
        return self.contacts