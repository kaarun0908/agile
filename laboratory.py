# laboratory.py

import tkinter as tk
from tkinter import ttk, messagebox
from database import prescriptions, lab_reports

report_count = 1001

def generate_report_id():
    global report_count
    report_id = f"LAB{report_count}"
    report_count += 1
    return report_id

def laboratory_module(parent):

    for widget in parent.winfo_children():
        widget.destroy()

    report_id = tk.StringVar(value=generate_report_id())
    patient = tk.StringVar()
    doctor = tk.StringVar()
    diagnosis = tk.StringVar()
    test_name = tk.StringVar()
    result = tk.StringVar()

    selected_index = None

    title = tk.Label(
        parent,
        text="LABORATORY MANAGEMENT",
        font=("Arial",20,"bold"),
        bg="#1565C0",
        fg="white",
        pady=10
    )

    title.pack(fill="x")

    form = tk.Frame(parent,padx=20,pady=20)
    form.pack()

    tk.Label(form,text="Report ID").grid(row=0,column=0,sticky="w",pady=5)
    tk.Entry(form,textvariable=report_id,state="readonly",width=30).grid(row=0,column=1)

    tk.Label(form,text="Patient").grid(row=1,column=0,sticky="w",pady=5)
    tk.Entry(form,textvariable=patient,state="readonly",width=30).grid(row=1,column=1)

    tk.Label(form,text="Doctor").grid(row=2,column=0,sticky="w",pady=5)
    tk.Entry(form,textvariable=doctor,state="readonly",width=30).grid(row=2,column=1)

    tk.Label(form,text="Diagnosis").grid(row=3,column=0,sticky="w",pady=5)
    tk.Entry(form,textvariable=diagnosis,state="readonly",width=30).grid(row=3,column=1)

    tk.Label(form,text="Test Name").grid(row=4,column=0,sticky="w",pady=5)
    tk.Entry(form,textvariable=test_name,width=30).grid(row=4,column=1)

    tk.Label(form,text="Result").grid(row=5,column=0,sticky="w",pady=5)
    tk.Entry(form,textvariable=result,width=30).grid(row=5,column=1)

    def refresh_table():

        for row in tree.get_children():
            tree.delete(row)

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

    def clear_fields():

        report_id.set(generate_report_id())
        patient.set("")
        doctor.set("")
        diagnosis.set("")
        test_name.set("")
        result.set("")

    def select_patient(event):

        nonlocal selected_index

        selected = tree.selection()

        if not selected:
            return

        selected_index = tree.index(selected)

        data = prescriptions[selected_index]

        patient.set(data["Patient"])
        doctor.set(data["Doctor"])
        diagnosis.set(data["Diagnosis"])

    def save_report():

        if patient.get()=="" or test_name.get()=="" or result.get()=="":

            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )

            return

        report = {

            "Report ID":report_id.get(),
            "Patient":patient.get(),
            "Doctor":doctor.get(),
            "Diagnosis":diagnosis.get(),
            "Test":test_name.get(),
            "Result":result.get()

        }

        lab_reports.append(report)

        messagebox.showinfo(
            "Success",
            "Laboratory Report Saved."
        )

        clear_fields()

    def search_patient():

        keyword = search_entry.get().lower()

        for row in tree.get_children():
            tree.delete(row)

        for item in prescriptions:

            if keyword in item["Patient"].lower():

                tree.insert(
                    "",
                    tk.END,
                    values=(
                        item["Patient"],
                        item["Doctor"],
                        item["Diagnosis"]
                    )
                )

    button_frame = tk.Frame(parent)
    button_frame.pack(pady=10)

    tk.Button(
        button_frame,
        text="Save Report",
        bg="green",
        fg="white",
        width=18,
        command=save_report
    ).grid(row=0,column=0,padx=5)

    tk.Button(
        button_frame,
        text="Clear",
        bg="orange",
        fg="white",
        width=15,
        command=clear_fields
    ).grid(row=0,column=1,padx=5)

    search_frame = tk.Frame(parent)
    search_frame.pack(pady=10)

    tk.Label(search_frame,text="Search Patient").pack(side="left")

    search_entry = tk.Entry(search_frame,width=30)
    search_entry.pack(side="left",padx=5)

    tk.Button(
        search_frame,
        text="Search",
        command=search_patient
    ).pack(side="left")

    tk.Button(
        search_frame,
        text="Show All",
        command=refresh_table
    ).pack(side="left",padx=5)

    columns=("Patient","Doctor","Diagnosis")

    tree = ttk.Treeview(
        parent,
        columns=columns,
        show="headings",
        height=10
    )

    for col in columns:

        tree.heading(col,text=col)
        tree.column(col,width=180)

    tree.pack(fill="both",expand=True,padx=20,pady=10)

    tree.bind("<<TreeviewSelect>>",select_patient)

    refresh_table()

