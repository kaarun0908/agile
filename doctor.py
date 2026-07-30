# doctor.py

import tkinter as tk
from tkinter import ttk, messagebox
from database import appointments, prescriptions

def doctor_module(parent):

    # Clear previous screen
    for widget in parent.winfo_children():
        widget.destroy()

    patient_name = tk.StringVar()
    doctor_name = tk.StringVar()
    diagnosis = tk.StringVar()
    medicine = tk.StringVar()

    selected_index = None

    # -------------------- Title --------------------

    title = tk.Label(
        parent,
        text="DOCTOR MODULE",
        font=("Arial", 20, "bold"),
        bg="#1565C0",
        fg="white",
        pady=10
    )
    title.pack(fill="x")

    # -------------------- Form --------------------

    form = tk.Frame(parent, padx=20, pady=20)
    form.pack()

    tk.Label(form, text="Patient Name").grid(row=0, column=0, pady=5, sticky="w")
    tk.Entry(form, textvariable=patient_name, state="readonly", width=30).grid(row=0, column=1)

    tk.Label(form, text="Doctor").grid(row=1, column=0, pady=5, sticky="w")
    tk.Entry(form, textvariable=doctor_name, state="readonly", width=30).grid(row=1, column=1)

    tk.Label(form, text="Diagnosis").grid(row=2, column=0, pady=5, sticky="w")
    tk.Entry(form, textvariable=diagnosis, width=30).grid(row=2, column=1)

    tk.Label(form, text="Medicine").grid(row=3, column=0, pady=5, sticky="w")
    tk.Entry(form, textvariable=medicine, width=30).grid(row=3, column=1)

    # -------------------- Functions --------------------

    def refresh_table():

        tree.delete(*tree.get_children())

        for item in appointments:

            tree.insert(
                "",
                tk.END,
                values=(
                    item["Appointment ID"],
                    item["Patient"],
                    item["Doctor"],
                    item["Date"],
                    item["Time"]
                )
            )

    def clear_fields():

        patient_name.set("")
        doctor_name.set("")
        diagnosis.set("")
        medicine.set("")

    def select_appointment(event):

        nonlocal selected_index

        selected = tree.focus()

        if not selected:
            return

        selected_index = tree.index(selected)

        data = tree.item(selected)["values"]

        patient_name.set(data[1])
        doctor_name.set(data[2])

    def save_prescription():

        if diagnosis.get() == "" or medicine.get() == "":

            messagebox.showerror(
                "Error",
                "Enter Diagnosis and Medicine."
            )
            return

        prescriptions.append({

            "Patient": patient_name.get(),
            "Doctor": doctor_name.get(),
            "Diagnosis": diagnosis.get(),
            "Medicine": medicine.get()

        })

        messagebox.showinfo(
            "Success",
            "Prescription Saved Successfully."
        )

        clear_fields()

    def search_patient():

        keyword = search_entry.get().lower()

        tree.delete(*tree.get_children())

        for item in appointments:

            if keyword in item["Patient"].lower():

                tree.insert(
                    "",
                    tk.END,
                    values=(
                        item["Appointment ID"],
                        item["Patient"],
                        item["Doctor"],
                        item["Date"],
                        item["Time"]
                    )
                )

    # -------------------- Buttons --------------------

    button_frame = tk.Frame(parent)
    button_frame.pack(pady=10)

    tk.Button(
        button_frame,
        text="Save Prescription",
        bg="green",
        fg="white",
        width=18,
        command=save_prescription
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Clear",
        bg="orange",
        fg="white",
        width=15,
        command=clear_fields
    ).grid(row=0, column=1, padx=5)

    # -------------------- Search --------------------

    search_frame = tk.Frame(parent)
    search_frame.pack(pady=10)

    tk.Label(search_frame, text="Search Patient").pack(side="left")

    search_entry = tk.Entry(search_frame, width=30)
    search_entry.pack(side="left", padx=5)

    tk.Button(
        search_frame,
        text="Search",
        command=search_patient
    ).pack(side="left")

    tk.Button(
        search_frame,
        text="Show All",
        command=refresh_table
    ).pack(side="left", padx=5)

    # -------------------- Table --------------------

    columns = (
        "Appointment ID",
        "Patient",
        "Doctor",
        "Date",
        "Time"
    )

    tree = ttk.Treeview(
        parent,
        columns=columns,
        show="headings",
        height=10
    )

    for col in columns:

        tree.heading(col, text=col)
        tree.column(col, width=140)

    tree.pack(fill="both", expand=True, padx=20, pady=10)

    tree.bind("<<TreeviewSelect>>", select_appointment)

    refresh_table()
