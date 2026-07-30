# pharmacy.py
 
import tkinter as tk
from tkinter import ttk, messagebox
from database import prescriptions
 
medicines = []
 
def pharmacy_module(parent):
 
    for widget in parent.winfo_children():
        widget.destroy()
 
    patient = tk.StringVar()
    medicine = tk.StringVar()
 
    tk.Label(parent, text="PHARMACY", font=("Arial", 18, "bold")).pack(pady=10)
 
    frame = tk.Frame(parent)
    frame.pack(pady=10)
 
    tk.Label(frame, text="Patient").grid(row=0, column=0, padx=5, pady=5)
    tk.Entry(frame, textvariable=patient, state="readonly").grid(row=0, column=1)
 
    tk.Label(frame, text="Medicine").grid(row=1, column=0, padx=5, pady=5)
    tk.Entry(frame, textvariable=medicine).grid(row=1, column=1)
 
    def load_patient(event):
        selected = tree.focus()
 
        if selected:
            data = tree.item(selected)["values"]
 
            patient.set(data[0])
 
    def issue_medicine():
 
        if patient.get() == "" or medicine.get() == "":
            messagebox.showerror("Error", "Fill all fields")
            return
 
        medicines.append({
            "Patient": patient.get(),
            "Medicine": medicine.get()
        })
 
        messagebox.showinfo("Success", "Medicine Issued")
 
        patient.set("")
        medicine.set("")
 
    tk.Button(
        parent,
        text="Issue Medicine",
        bg="green",
        fg="white",
        command=issue_medicine
    ).pack(pady=10)
 
    columns = ("Patient", "Doctor", "Diagnosis")
 
    tree = ttk.Treeview(parent, columns=columns, show="headings", height=10)
 
    for col in columns:
        tree.heading(col, text=col)
 
    for item in prescriptions:
        tree.insert(
            "",
            tk.END,
            values=(
                item["Patient"],
                item["Doctor"],
                item["Diagnosis"]
            )
        )
 
    tree.pack(padx=10, pady=10)
 
    tree.bind("<<TreeviewSelect>>", load_patient)