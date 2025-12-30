def get_input():
    print(f"Getting user input")

def validate_input():
    print("Validating the user info")

def save_to_db():
    print(f"Saving to DB")

def registerUser():
    get_input()
    validate_input()
    save_to_db()
    print(f"User registration complete")
    
registerUser()