# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 11:20:28 2026

@author: Ashik
"""

import tkinter as tk
from tkinter import messagebox,ttk
from PIL import Image,ImageTk,ImageFilter
import pymysql
from tkcalendar import DateEntry


def connect_db():
   return pymysql.connect(
        host="localhost",
        user="root",
        password="Jenish@2003",
        database="vehicle"
        )

def submit():
    name = name_entry.get()
    number = number_entry.get()
    reg_num = reg_num_entry.get()
    Vehicle_Model = combo_Vehicle_Model.get()
    Service_Type = combo_Service_Type.get()
    date = date_entry.get()
    mechanic = combo_mechanic.get()
    status = listbox.get(listbox.curselection()) if listbox.curselection() else ""


    if not all([name,number,reg_num,Vehicle_Model,Service_Type,date,mechanic,status]):
        messagebox.showerror("Error","Please fil all required fields.")
        return

    conn = connect_db()
    cur = conn.cursor()

    if selected_id.get() == 0:
        cur.execute("INSERT INTO customer_details ( CUSTOMER_NAME,CUSTOMER_NUMBER,REGISTER_NUMBER,VEHICLE_MODEL,SERVICE_TYPE,SERVICE_DATE,ASSIGNED_MECHANIC,SERVICE_STATUS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                     (name,number,reg_num,Vehicle_Model,Service_Type,date,mechanic,status))

    else:
        cur.execute("UPDATE customer_details SET CUSTOMER_NAME=%s,CUSTOMER_NUMBER=%s,REGISTER_NUMBER=%s,VEHICLE_MODEL=%s,SERVICE_TYPE=%s,SERVICE_DATE=%s,ASSIGNED_MECHANIC=%s,SERVICE_STATUS=%s WHERE id=%s",
                     (name,number,reg_num,Vehicle_Model,Service_Type,date,mechanic,status,selected_id.get()))

    conn.commit()
    conn.close()
    fetch_data()
    clear()
    messagebox.showinfo("Success","Data saved/updated successfully!")

def clear():
    name_entry.delete(0,tk.END)
    number_entry.delete(0,tk.END)
    reg_num_entry.delete(0,tk.END)
    combo_Vehicle_Model.set("")
    combo_Service_Type.set("")
    date_entry.delete(0,tk.END)
    combo_mechanic.set("")
    listbox.selection_clear(0,tk.END)
    selected_id.set(0)
    

def fetch_data():
    for item in tree.get_children():
        tree.delete(item)

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer_details")
    for row in cur.fetchall():
        tree.insert("",tk.END,values=row)
    conn.close()

def on_tree_select(event):
    clear()
    selected = tree.focus()
    values = tree.item(selected,'values')
    if values:
        selected_id.set(values[0])
        name_entry.insert(0,values[1])
        number_entry.insert(0,values[2])
        reg_num_entry.insert(0,values[3])
        combo_Vehicle_Model.set(values[4])
        combo_Service_Type.set(values[5])
        date_entry.insert(0,values[6])
        combo_mechanic.set(values[7])
        for i in range(listbox.size()):
            if listbox.get(i) == values[8]:
                listbox.selection_set(i)


def delete_record():
    if selected_id.get() == 0:
        messagebox.showwarning("warning","Selected a record to delete.")
        return
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM customer_details WHERE id=%s",(selected_id.get(),))
    conn.commit()
    conn.close()
    fetch_data()
    clear()
    messagebox.showinfo("Deleted","Record Deleted Successfully.")


# === GUI Setup ===
root=tk.Tk()
root.title("Tkinter MySQL Form")
root.geometry("900x600")
img=Image.open(r"C:\Users\Ashik\Downloads\CARR.jpeg")
img_path = img.resize((1550, 800))
tk_img=ImageTk.PhotoImage(img_path)
label=tk.Label(root,image=tk_img)
label.place(x=0,y=0)

frame = tk.Frame(root,bg = "darkorchid4",padx=10,pady=10)
frame.pack()

selected_id = tk.IntVar(value=0)

# === From UI ===
tk.Label(frame, text="CUSTOMER NAME",fg="white",bg = "darkorchid4",font=('Arial',13,'bold')).grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, width=40)
name_entry.grid(row=0,column=2)

tk.Label(frame, text="CUSTOMER NUMBER", fg="white",bg = "darkorchid4", font=('Arial', 13, 'bold')).grid(row=1, column=0, sticky="w")
number_entry = tk.Entry(frame, width=40)
number_entry.grid(row=1, column=2)

tk.Label(frame, text="REGISTRATION NUMBER", fg="white",bg = "darkorchid4", font=('Arial', 13, 'bold')).grid(row=2, column=0, sticky="w")
reg_num_entry = tk.Entry(frame, width=40)
reg_num_entry.grid(row=2, column=2)

tk.Label(frame, text="VEHICLE MODEL", fg="white",bg = "darkorchid4", font=('Arial', 13, 'bold')).grid(row=3, column=0, sticky="w")
combo_Vehicle_Model= ttk.Combobox(frame,values=['Hyundai Creta','Mahindra XUV700','Tata Nexon','Maruti Suzuki Brezz','Toyota Urban Cruiser Hyryder'], state="readonly", width=27)
combo_Vehicle_Model.grid(row=3, column=2, sticky="w")

tk.Label(frame, text="SERVICE TYPE", fg="white",bg = "darkorchid4", font=('Arial', 13, 'bold')).grid(row=4, column=0, sticky="w")
combo_Service_Type= ttk.Combobox(frame,values=['Oil Change','Engine Check','Full Service','A/C Service','Wheel Alignment'], state="readonly", width=27)
combo_Service_Type.grid(row=4, column=2, sticky="w")

tk.Label(frame, text="SERVICE DATE",fg="white",bg = "darkorchid4",font=('Arial',13,'bold')).grid(row=5, column=0, sticky="w")
date_entry = DateEntry(frame,width=27,background="darkblue",foreground="white",borderwidth=2,date_pattern="yyyy-mm-dd")
date_entry.grid(row=5, column=2, sticky="w")


tk.Label(frame, text="ASSIGNED MECHANIC", fg="white",bg = "darkorchid4", font=('Arial', 13, 'bold')).grid(row=6, column=0, sticky="w")
combo_mechanic= ttk.Combobox(frame,values=['Mady','Siva','Alex','John','Matthew'], state="readonly", width=27)
combo_mechanic.grid(row=6, column=2, sticky="w")

tk.Label(frame, text="SERVICE STATUS", fg="white",bg = "darkorchid4", font=('Arial', 13, 'bold')).grid(row=7, column=0, sticky="nw")
listbox = tk.Listbox(frame,fg="white",bg = "darkorchid4",font=('Arial', 10, 'bold'), height=4)
for item in ["PENDING", "IN PROGRESS", "COMPLETED"]:
    listbox.insert(tk.END, item)
listbox.grid(row=7, column=2, sticky="w")



# === Buttons ===
tk.Button(frame, text="Submit", fg="white",font=('Arial', 13, 'bold'), bg="blue", command=submit).grid(row=10, column=2, pady=10, sticky="e")
tk.Button(frame, text="Clear", fg="white", font=('Arial', 13, 'bold'),bg="blue", command=clear).grid(row=10, column=1, pady=10)
tk.Button(frame, text="Delete", fg="white",font=('Arial', 13, 'bold'), bg="blue", command=delete_record).grid(row=10, column=0, sticky="w")

# === Treeview Table (Aligned Columns) ===

style = ttk.Style()
style.theme_use("clam")

# Header style
style.configure("Treeview.Heading",font=('Arial', 10, 'bold'),background="dodger blue3",foreground="white")

# Treeview body style
style.configure("Treeview",background="medium purple4",foreground="white",fieldbackground="mudium purple4",rowheight=28)

# Selected row color
style.map("Treeview",background=[("selected", "dodger blue3")],foreground=[("selected", "white")])


'''

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
style.configure("Treeview", font=('Arial', 10), rowheight=25)
'''
tree = ttk.Treeview(root, columns=("ID","CUSTOMER_NAME","CUSTOMER_NUMBER","REGISTER_NUMBER","VEHICLE_MODEL","SERVICE_TYPE","SERVICE_DATE","ASSIGNED_MECHANIC","SERVICE_STATUS"), show="headings", height=6)

tree.heading("ID", text="ID")
tree.column("ID", width=40, anchor="center")

tree.heading("CUSTOMER_NAME", text="CUSTOMER NAME")
tree.column("CUSTOMER_NAME", width=108, anchor="w")

tree.heading("CUSTOMER_NUMBER", text="CUSTOMER NUMBER")
tree.column("CUSTOMER_NUMBER", width=108, anchor="w")

tree.heading("REGISTER_NUMBER", text="REGISTER NUMBER")
tree.column("REGISTER_NUMBER", width=108, anchor="center")

tree.heading("VEHICLE_MODEL", text="VEHICLE MODEL")
tree.column("VEHICLE_MODEL", width=100, anchor="center")

tree.heading("SERVICE_TYPE", text="SERVICE TYPE")
tree.column("SERVICE_TYPE", width=100, anchor="w")

tree.heading("SERVICE_DATE",text="SERVICE DATE")
tree.column("SERVICE_DATE",width=100,anchor="w")

tree.heading("ASSIGNED_MECHANIC",text="ASSIGNED MECHANIC")
tree.column("ASSIGNED_MECHANIC",width=100,anchor="w")

tree.heading("SERVICE_STATUS",text="SERVICE STATUS")
tree.column("SERVICE_STATUS",width=100,anchor="w")

tree.pack(pady=20, fill="x")
tree.bind("<<TreeviewSelect>>", on_tree_select)




fetch_data()
root.mainloop()







    


