# billing.py

import tkinter as tk
from tkinter import ttk, messagebox
from database import patients

bills = []

def billing_module(parent):

    for widget in parent.winfo_children():
        widget.destroy()

    patient = tk.StringVar()
    amount = tk.StringVar()

    tk.Label(parent,
             text="BILLING",
             font=("Arial",18,"bold")).pack(pady=10)

    frame = tk.Frame(parent)
    frame.pack(pady=10)

    tk.Label(frame,text="Patient").grid(row=0,column=0,padx=5,pady=5)

    patient_box = ttk.Combobox(
        frame,
        textvariable=patient,
        values=[p["Name"] for p in patients],
        state="readonly",
        width=25
    )

    patient_box.grid(row=0,column=1)

    tk.Label(frame,text="Amount").grid(row=1,column=0,padx=5,pady=5)

    tk.Entry(frame,textvariable=amount,width=28).grid(row=1,column=1)

    def generate_bill():

        if patient.get()=="" or amount.get()=="":

            messagebox.showerror("Error","Fill all fields")
            return

        bills.append({
            "Patient":patient.get(),
            "Amount":amount.get()
        })

        tree.insert(
            "",
            tk.END,
            values=(patient.get(),amount.get())
        )

        messagebox.showinfo("Success","Bill Generated")

        patient.set("")
        amount.set("")

    tk.Button(
        parent,
        text="Generate Bill",
        bg="green",
        fg="white",
        command=generate_bill
    ).pack(pady=10)

    columns=("Patient","Amount")

    tree=ttk.Treeview(
        parent,
        columns=columns,
        show="headings",
        height=10
    )

    tree.heading("Patient",text="Patient")
    tree.heading("Amount",text="Amount")

    tree.column("Patient",width=200)
    tree.column("Amount",width=150)

    tree.pack(pady=10)

    for bill in bills:

        tree.insert(
            "",
            tk.END,
            values=(
                bill["Patient"],
                bill["Amount"]
            )
        )

