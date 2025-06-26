def input_name(prompt):
    value = input(prompt).strip()
    if not value.replace(" ", "").isalpha():
        print("Error: The contact’s name must be a string.")
        return None
    return value

def input_phone(prompt):
    value = input(prompt).strip()
    if not value.isdigit():
        print("Error: The phone number must be an integer.")
        return None
    return value

def input_email(prompt):
    value = input(prompt).strip()
    if "@" not in value or "." not in value:
        print("Error: Please enter a valid email address.")
        return None
    return value

def input_address(prompt):
    value = input(prompt).strip()
    if not value:
        print("Error: Address cannot be empty.")
        return None
    return value