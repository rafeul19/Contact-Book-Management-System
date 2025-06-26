# Define the Person class to represent a contact
class Person:
    # Initialize a Person object with name, phone, email, and address
    def __init__(self, name, phone, email, address):
        self.name = name      # Store the contact's name
        self.phone = phone    # Store the contact's phone number
        self.email = email    # Store the contact's email address
        self.address = address # Store the contact's address

    # Convert the Person object to a dictionary for CSV writing
    def to_dict(self):
        return {
            "name": self.name,         # Key: name, Value: contact's name
            "phone": self.phone,       # Key: phone, Value: contact's phone
            "email": self.email,       # Key: email, Value: contact's email
            "address": self.address    # Key: address, Value: contact's address
        }

    # Create a Person object from a dictionary (e.g., from CSV row)
    @staticmethod
    def from_dict(data):
        return Person(
            data.get("name", ""),      # Get name from dict, default to empty string
            data.get("phone", ""),     # Get phone from dict, default to empty string
            data.get("email", ""),     # Get email from dict, default to empty string
            data.get("address", "")    # Get address from dict, default to empty string
        )