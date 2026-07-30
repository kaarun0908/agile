# patient.py
 
import tkinter as tk
from tkinter import ttk, messagebox
from database import patients
 
patient_count = 1001
 
def generate_patient_id():
    global patient_count
    patient_id = f"PAT{patient_count}"
    patient_count += 1
    return patient_id
 
def patient_module(parent):
 
    # ------------------------
    # Clear Previous Widgets
    # ------------------------
 
    for widget in parent.winfo_children():
        widget.destroy()
 
    # ------------------------
    # Variables
    # ------------------------
 
    patient_id = tk.StringVar(value=generate_patient_id())
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    phone = tk.StringVar()
    address = tk.StringVar()
    disease = tk.StringVar()
 
    selected_index = None
 
    # ------------------------
    # Title
    # ------------------------
 
    title = tk.Label(
        parent,
        text="PATIENT REGISTRATION",
        font=("Arial", 20, "bold"),
        bg="#1565C0",
        fg="white",
        pady=10
    )
 
    title.pack(fill="x")
 
    # ------------------------
    # Form
    # ------------------------
 
    form = tk.Frame(parent, padx=20, pady=20)
    form.pack()
 
    # Patient ID
 
    tk.Label(form, text="Patient ID", font=("Arial",11)).grid(row=0,column=0,pady=5,sticky="w")
 
    tk.Entry(
        form,
        textvariable=patient_id,
        state="readonly",
        width=30
    ).grid(row=0,column=1,pady=5)
 
    # Name
 
    tk.Label(form,text="Name",font=("Arial",11)).grid(row=1,column=0,pady=5,sticky="w")
 
    tk.Entry(
        form,
        textvariable=name,
        width=30
    ).grid(row=1,column=1,pady=5)
 
    # Age
 
    tk.Label(form,text="Age",font=("Arial",11)).grid(row=2,column=0,pady=5,sticky="w")
 
    tk.Entry(
        form,
        textvariable=age,
        width=30
    ).grid(row=2,column=1,pady=5)
 
    # Gender
 
    tk.Label(form,text="Gender",font=("Arial",11)).grid(row=3,column=0,pady=5,sticky="w")
 
    gender_box = ttk.Combobox(
        form,
        textvariable=gender,
        values=["Male","Female","Other"],
        width=27,
        state="readonly"
    )
 
    gender_box.grid(row=3,column=1,pady=5)
 
    # Phone
 
    tk.Label(form,text="Phone",font=("Arial",11)).grid(row=4,column=0,pady=5,sticky="w")
 
    tk.Entry(
        form,
        textvariable=phone,
        width=30
    ).grid(row=4,column=1,pady=5)
 
    # Address
 
    tk.Label(form,text="Address",font=("Arial",11)).grid(row=5,column=0,pady=5,sticky="w")
 
    tk.Entry(
        form,
        textvariable=address,
        width=30
    ).grid(row=5,column=1,pady=5)
 
    # Disease
 
    tk.Label(form,text="Disease",font=("Arial",11)).grid(row=6,column=0,pady=5,sticky="w")
 
    tk.Entry(
        form,
        textvariable=disease,
        width=30
    ).grid(row=6,column=1,pady=5)
 
    # ------------------------
    # Functions
    # ------------------------
 
    def clear_fields():
 
        patient_id.set(generate_patient_id())
        name.set("")
        age.set("")
        gender.set("")
        phone.set("")
        address.set("")
        disease.set("")
 
    def refresh_table():
 
        for row in tree.get_children():
            tree.delete(row)
 
        for patient in patients:
 
            tree.insert(
                "",
                tk.END,
                values=(
                    patient["Patient ID"],
                    patient["Name"],
                    patient["Age"],
                    patient["Gender"],
                    patient["Phone"],
                    patient["Address"],
                    patient["Disease"]
                )
            )
 
    def add_patient():
 
        if name.get()=="" or age.get()=="" or gender.get()=="":
 
            messagebox.showerror(
                "Error",
                "Please fill all required fields."
            )
 
            return
 
        patient = {
 
            "Patient ID":patient_id.get(),
            "Name":name.get(),
            "Age":age.get(),
            "Gender":gender.get(),
            "Phone":phone.get(),
            "Address":address.get(),
            "Disease":disease.get()
 
        }
 
        patients.append(patient)
 
        refresh_table()
 
        messagebox.showinfo(
            "Success",
            "Patient Registered Successfully."
        )
 
        clear_fields()
 
    def delete_patient():
 
        selected = tree.selection()
 
        if not selected:
 
            messagebox.showwarning(
                "Warning",
                "Select a patient."
            )
 
            return
 
        index = tree.index(selected)
 
        patients.pop(index)
 
        refresh_table()
 
        clear_fields()
 
    def search_patient():
 
        keyword = search_entry.get().lower()
 
        for row in tree.get_children():
            tree.delete(row)
 
        for patient in patients:
 
            if keyword in patient["Name"].lower():
 
                tree.insert(
                    "",
                    tk.END,
                    values=(
                        patient["Patient ID"],
                        patient["Name"],
                        patient["Age"],
                        patient["Gender"],
                        patient["Phone"],
                        patient["Address"],
                        patient["Disease"]
                    )
                )
 
    def select_patient(event):
 
        nonlocal selected_index
 
        selected = tree.selection()
 
        if not selected:
            return
 
        selected_index = tree.index(selected)
 
        data = patients[selected_index]
 
        patient_id.set(data["Patient ID"])
        name.set(data["Name"])
        age.set(data["Age"])
        gender.set(data["Gender"])
        phone.set(data["Phone"])
        address.set(data["Address"])
        disease.set(data["Disease"])
 
    def update_patient():
 
        if selected_index is None:
 
            messagebox.showwarning(
                "Warning",
                "Select a patient."
            )
 
            return
 
        patients[selected_index] = {
 
            "Patient ID":patient_id.get(),
            "Name":name.get(),
            "Age":age.get(),
            "Gender":gender.get(),
            "Phone":phone.get(),
            "Address":address.get(),
            "Disease":disease.get()
 
        }
 
        refresh_table()
 
        messagebox.showinfo(
            "Updated",
            "Patient Updated Successfully."
        )
 
        clear_fields()
 
    # ------------------------
    # Buttons
    # ------------------------
 
    button_frame = tk.Frame(parent)
    button_frame.pack(pady=10)
 
    tk.Button(
        button_frame,
        text="Add Patient",
        bg="green",
        fg="white",
        width=15,
        command=add_patient
    ).grid(row=0,column=0,padx=5)
 
    tk.Button(
        button_frame,
        text="Update",
        bg="blue",
        fg="white",
        width=15,
        command=update_patient
    ).grid(row=0,column=1,padx=5)
 
    tk.Button(
        button_frame,
        text="Delete",
        bg="red",
        fg="white",
        width=15,
        command=delete_patient
    ).grid(row=0,column=2,padx=5)
 
    tk.Button(
        button_frame,
        text="Clear",
        bg="orange",
        fg="white",
        width=15,
        command=clear_fields
    ).grid(row=0,column=3,padx=5)
 
    # ------------------------
    # Search
    # ------------------------
 
    search_frame = tk.Frame(parent)
    search_frame.pack(pady=10)
 
    tk.Label(
        search_frame,
        text="Search Name:"
    ).pack(side="left")
 
    search_entry = tk.Entry(search_frame,width=30)
 
    search_entry.pack(side="left",padx=5)
 
    tk.Button(
        search_frame,
        text="Search",
        command=search_patient
    ).pack(side="left")
 
    # ------------------------
    # Table
    # ------------------------
 
    columns = (
        "ID",
        "Name",
        "Age",
        "Gender",
        "Phone",
        "Address",
        "Disease"
    )
 
    tree = ttk.Treeview(
        parent,
        columns=columns,
        show="headings",
        height=10
    )
 
    for col in columns:
 
        tree.heading(col,text=col)
        tree.column(col,width=120)
 
    tree.pack(fill="both",expand=True,padx=20,pady=10)
 
    tree.bind("<<TreeviewSelect>>",select_patient)
 
    refresh_table()