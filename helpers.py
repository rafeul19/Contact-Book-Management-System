# Validate and get a name input from the user
def input_name(prompt):
    value = input(prompt).strip()                        # Get user input and remove whitespace
    if not value.replace(" ", "").isalpha():             # Check if name contains only letters and spaces
        print("Error: The contact’s name must be a string.") # Print error if invalid
        return None
    return value                                         # Return valid name

# Validate and get a phone number input from the user
def input_phone(prompt):
    value = input(prompt).strip()                        # Get user input and remove whitespace
    if not value.isdigit():                              # Check if phone is all digits
        print("Error: The phone number must be an integer.") # Print error if invalid
        return None
    return value                                         # Return valid phone

# Validate and get an email input from the user
def input_email(prompt):
    value = input(prompt).strip()                        # Get user input and remove whitespace
    if "@" not in value or "." not in value:             # Check for basic email format
        print("Error: Please enter a valid email address.") # Print error if invalid
        return None
    return value                                         # Return valid email

# Validate and get an address input from the user
def input_address(prompt):
    value = input(prompt).strip()                        # Get user input and remove whitespace
    if not value:                                        # Check if address is not empty
        print("Error: Address cannot be empty.")         # Print error if empty
        return None
    return value                                         # Return valid address