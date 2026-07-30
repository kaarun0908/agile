import tkinter as tk
from tkinter import ttk, messagebox
from database import appointments, patients, doctors, time_slots

appointment_count = 1001

def generate_appointment_id():
    global appointment_count
    appointment_id = f"APT{appointment_count}"
    appointment_count += 1
    return appointment_id

def appointment_module(parent):

    for widget in parent.winfo_children():
        widget.destroy()

    appointment_id = tk.StringVar(value=generate_appointment_id())
    patient_name = tk.StringVar()
    doctor = tk.StringVar()
    date = tk.StringVar()
    time = tk.StringVar()

    selected_index = None

    title = tk.Label(
        parent,
        text="APPOINTMENT AND MANAGEMENT",
        font=("Arial",20,"bold"),
        bg="#1565C0",
        fg="white",
        pady=10
    )

    title.pack(fill="x")

    form = tk.Frame(parent,padx=20,pady=20)
    form.pack()

    tk.Label(form,text="Appointment ID").grid(row=0,column=0,sticky="w",pady=5)

    tk.Entry(
        form,
        textvariable=appointment_id,
        state="readonly",
        width=30
    ).grid(row=0,column=1)

    tk.Label(form,text="Patient").grid(row=1,column=0,sticky="w",pady=5)

    patient_names=[]

    for p in patients:
        patient_names.append(p["Name"])

    patient_box=ttk.Combobox(
        form,
        textvariable=patient_name,
        values=patient_names,
        width=27,
        state="readonly"
    )

    patient_box.grid(row=1,column=1)

    tk.Label(form,text="Doctor").grid(row=2,column=0,sticky="w",pady=5)

    doctor_box=ttk.Combobox(
        form,
        textvariable=doctor,
        values=doctors,
        width=27,
        state="readonly"
    )

    doctor_box.grid(row=2,column=1)

    tk.Label(form,text="Date").grid(row=3,column=0,sticky="w",pady=5)

    tk.Entry(
        form,
        textvariable=date,
        width=30
    ).grid(row=3,column=1)

    tk.Label(form,text="Time").grid(row=4,column=0,sticky="w",pady=5)

    time_box=ttk.Combobox(
        form,
        textvariable=time,
        values=time_slots,
        width=27,
        state="readonly"
    )

    time_box.grid(row=4,column=1)

    def refresh_table():

        for row in tree.get_children():
            tree.delete(row)

        for appointment in appointments:

            tree.insert(
                "",
                tk.END,
                values=(
                    appointment["Appointment ID"],
                    appointment["Patient"],
                    appointment["Doctor"],
                    appointment["Date"],
                    appointment["Time"]
                )
            )

    def clear_fields():

        appointment_id.set(generate_appointment_id())
        patient_name.set("")
        doctor.set("")
        date.set("")
        time.set("")

          # ------------------------
    # Search Frame
    # ------------------------

    search_frame = tk.Frame(parent)
    search_frame.pack(pady=10)

    tk.Label(
        search_frame,
        text="Search Patient :",
        font=("Arial",11)
    ).pack(side="left")

    search_entry = tk.Entry(search_frame,width=30)
    search_entry.pack(side="left",padx=5)

    # ------------------------
    # Remaining Functions
    # ------------------------

    def select_appointment(event):

        nonlocal selected_index

        selected = tree.selection()

        if not selected:
            return

        selected_index = tree.index(selected)

        data = appointments[selected_index]

        appointment_id.set(data["Appointment ID"])
        patient_name.set(data["Patient"])
        doctor.set(data["Doctor"])
        date.set(data["Date"])
        time.set(data["Time"])

    def update_appointment():

        if selected_index is None:

            messagebox.showwarning(
                "Warning",
                "Please select an appointment."
            )

            return

        appointments[selected_index] = {

            "Appointment ID": appointment_id.get(),
            "Patient": patient_name.get(),
            "Doctor": doctor.get(),
            "Date": date.get(),
            "Time": time.get()

        }

        refresh_table()

        messagebox.showinfo(
            "Updated",
            "Appointment Updated Successfully."
        )

        clear_fields()

    def delete_appointment():

        selected = tree.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select an appointment."
            )

            return

        index = tree.index(selected)

        del appointments[index]

        refresh_table()

        clear_fields()

        messagebox.showinfo(
            "Deleted",
            "Appointment Deleted Successfully."
        )

    def search_appointment():

        keyword = search_entry.get().lower()

        for row in tree.get_children():
            tree.delete(row)

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

    # ------------------------
    # Configure Buttons
    # ------------------------

    # Replace the placeholder buttons with these:

    for widget in button_frame.winfo_children():
        widget.destroy()

    tk.Button(
        button_frame,
        text="Book",
        bg="green",
        fg="white",
        width=15,
        command=book_appointment
    ).grid(row=0,column=0,padx=5)

    tk.Button(
        button_frame,
        text="Update",
        bg="blue",
        fg="white",
        width=15,
        command=update_appointment
    ).grid(row=0,column=1,padx=5)

    tk.Button(
        button_frame,
        text="Delete",
        bg="red",
        fg="white",
        width=15,
        command=delete_appointment
    ).grid(row=0,column=2,padx=5)

    tk.Button(
        button_frame,
        text="Clear",
        bg="orange",
        fg="white",
        width=15,
        command=clear_fields
    ).grid(row=0,column=3,padx=5)

    tk.Button(
        search_frame,
        text="Search",
        bg="#1565C0",
        fg="white",
        width=12,
        command=search_appointment
    ).pack(side="left")

    tk.Button(
        search_frame,
        text="Show All",
        bg="gray",
        fg="white",
        width=12,
        command=refresh_table
    ).pack(side="left",padx=5)

    tree.bind("<<TreeviewSelect>>", select_appointment)

    def book_appointment():

        if patient_name.get()=="" or doctor.get()=="" or date.get()=="" or time.get()=="":

            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )

            return

        for item in appointments:

            if item["Doctor"]==doctor.get() and \
               item["Date"]==date.get() and \
               item["Time"]==time.get():

                messagebox.showerror(
                    "Unavailable",
                    "Doctor already booked for this slot."
                )

                return

        appointment={

            "Appointment ID":appointment_id.get(),
            "Patient":patient_name.get(),
            "Doctor":doctor.get(),
            "Date":date.get(),
            "Time":time.get()

        }

        appointments.append(appointment)

        refresh_table()

        messagebox.showinfo(
            "Success",
            "Appointment Booked Successfully."
        )

        clear_fields()

    button_frame=tk.Frame(parent)
    button_frame.pack(pady=10)

    tk.Button(
        button_frame,
        text="Book Appointment",
        bg="green",
        fg="white",
        width=18,
        command=book_appointment
    ).grid(row=0,column=0,padx=5)

    tk.Button(
        button_frame,
        text="Update",
        bg="blue",
        fg="white",
        width=15
    ).grid(row=0,column=1,padx=5)

    tk.Button(
        button_frame,
        text="Delete",
        bg="red",
        fg="white",
        width=15
    ).grid(row=0,column=2,padx=5)

    tk.Button(
        button_frame,
        text="Clear",
        bg="orange",
        fg="white",
        width=15,
        command=clear_fields
    ).grid(row=0,column=3,padx=5)

    columns=("ID","Patient","Doctor","Date","Time")

    tree=ttk.Treeview(
        parent,
        columns=columns,
        show="headings",
        height=10
    )

    for col in columns:

        tree.heading(col,text=col)
        tree.column(col,width=150)

    tree.pack(fill="both",expand=True,padx=20,pady=10)

    refresh_table()
