print("Starting Hospital Management System test...")

from patient import patient_module
print("Patient module: OK")

from appointment import appointment_module
print("Appointment module: OK")

from doctor import doctor_module
print("Doctor module: OK")

from laboratory import laboratory_module
print("Laboratory module: OK")

from pharmacy import pharmacy_module
print("Pharmacy module: OK")

from billing import billing_module
print("Billing module: OK")

from users import validate_login
print("Users module: OK")

print()
print("All modules imported successfully!")
print("Hospital Management System build test passed!")