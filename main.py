import tkinter as tk
from tkinter import messagebox
 
from patient import patient_module
from appointment import appointment_module
from doctor import doctor_module
from laboratory import laboratory_module
from pharmacy import pharmacy_module
from billing import billing_module
from users import validate_login
 
root = tk.Tk()
root.title("Hospital management and  System")
root.geometry("1100x650")
 
# ---------------- Login ----------------
 
login_frame = tk.Frame(root)
login_frame.pack(expand=True)
 
tk.Label(login_frame,
         text="Hospital Management System",
         font=("Arial",20,"bold")).pack(pady=20)
 
tk.Label(login_frame,text="Username").pack()
username_entry = tk.Entry(login_frame,width=30)
username_entry.pack()
 
tk.Label(login_frame,text="Password").pack()
password_entry = tk.Entry(login_frame,width=30,show="*")
password_entry.pack(pady=5)
 
def open_dashboard():
 
    login_frame.destroy()
 
    menu = tk.Frame(root,bg="lightblue",width=200)
    menu.pack(side="left",fill="y")
 
    content = tk.Frame(root)
    content.pack(side="right",fill="both",expand=True)
 
    tk.Button(menu,text="Patient",width=20,
              command=lambda: patient_module(content)).pack(pady=10)
 
    tk.Button(menu,text="Appointment",width=20,
              command=lambda: appointment_module(content)).pack(pady=10)
 
    tk.Button(menu,text="Doctor",width=20,
              command=lambda: doctor_module(content)).pack(pady=10)
 
    tk.Button(menu,text="Laboratory",width=20,
              command=lambda: laboratory_module(content)).pack(pady=10)
 
    tk.Button(menu,text="Pharmacy",width=20,
              command=lambda: pharmacy_module(content)).pack(pady=10)
 
    tk.Button(menu,text="Billing",width=20,
              command=lambda: billing_module(content)).pack(pady=10)
 
def login():
 
    username = username_entry.get()
    password = password_entry.get()
 
    status, role = validate_login(username,password)
 
    if status:
        messagebox.showinfo("Success","Login Successful")
        open_dashboard()
    else:
        messagebox.showerror("Error","Invalid Username or Password")
 
tk.Button(login_frame,
          text="Login",
          bg="green",
          fg="white",
          command=login).pack(pady=15)
 
root.mainloop()