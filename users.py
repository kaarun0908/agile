# users.py
 
# Built-in users for login
 
USERS = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
 
    "reception": {
        "password": "recep123",
        "role": "Receptionist"
    },
 
    "doctor": {
        "password": "doctor123",
        "role": "Doctor"
    },
 
    "lab": {
        "password": "lab123",
        "role": "Laboratory Technician"
    },
 
    "pharmacy": {
        "password": "pharma123",
        "role": "Pharmacist"
    },
 
    "cashier": {
        "password": "cash123",
        "role": "Cashier"
    }
}
 
def validate_login(username, password):
    """
    Check username and password.
    Returns (True, role) if valid.
    Returns (False, None) if invalid.
    """
 
    if username in USERS:
        if USERS[username]["password"] == password:
            return True, USERS[username]["role"]
 
    return False, None
 