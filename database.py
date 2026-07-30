# database.py

# ==========================
# HOSPITAL MANAGEMENT SYSTEM
# In-Memory Database
# ==========================

# --------------------------
# Patient Records
# --------------------------
patients = []

# Example Format:
# {
#     "Patient ID": "PAT1001",
#     "Name": "John",
#     "Age": 25,
#     "Gender": "Male",
#     "Phone": "9876543210",
#     "Address": "Chennai",
#     "Disease": "Fever"
# }

# --------------------------
# Appointment Records
# --------------------------
appointments = []

# Example Format:
# {
#     "Appointment ID": "APT1001",
#     "Patient ID": "PAT1001",
#     "Patient Name": "John",
#     "Doctor": "Dr. Smith",
#     "Date": "20/08/2026",
#     "Time": "10:00 AM"
# }

# --------------------------
# Prescription Records
# --------------------------
prescriptions = []

# Example Format:
# {
#     "Prescription ID": "PRE1001",
#     "Patient ID": "PAT1001",
#     "Doctor": "Dr. Smith",
#     "Diagnosis": "Viral Fever",
#     "Medicines": "Paracetamol",
#     "Remarks": "Take rest"
# }

# --------------------------
# Laboratory Reports
# --------------------------
lab_reports = []

# Example Format:
# {
#     "Lab ID": "LAB1001",
#     "Patient ID": "PAT1001",
#     "Test": "Blood Test",
#     "Result": "Normal"
# }

# --------------------------
# Pharmacy Records
# --------------------------
pharmacy_records = []

# Example Format:
# {
#     "Issue ID": "MED1001",
#     "Patient ID": "PAT1001",
#     "Medicine": "Paracetamol",
#     "Quantity": 10
# }

# --------------------------
# Billing Records
# --------------------------
bills = []

# Example Format:
# {
#     "Bill ID": "BILL1001",
#     "Patient ID": "PAT1001",
#     "Consultation": 500,
#     "Lab": 300,
#     "Medicine": 250,
#     "Total": 1050
# }

# --------------------------
# Doctor List
# --------------------------
doctors = [
    "Dr. John",
    "Dr. Smith",
    "Dr. Alice",
    "Dr. David",
    "Dr. Priya"
]

# --------------------------
# Doctor Available Time Slots
# --------------------------
time_slots = [
    "09:00 AM",
    "10:00 AM",
    "11:00 AM",
    "12:00 PM",
    "02:00 PM",
    "03:00 PM",
    "04:00 PM"
]

# --------------------------
# Medicine Inventory
# --------------------------
medicine_inventory = {
    "Paracetamol": 100,
    "Amoxicillin": 50,
    "Ibuprofen": 80,
    "Vitamin C": 120,
    "Cough Syrup": 40,
    "Cetirizine": 60,
    "Azithromycin": 45
}

lab_reports = []
prescriptions = []
