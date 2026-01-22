# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 11:05:45 2026

@author: Ashik
"""

import tkinter as tk
from tkinter import font,messagebox,ttk
from PIL import Image,ImageTk,ImageFilter
import pymysql
import subprocess
import sys  
import os

def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Jenish@2003",
        database="vehicle"
        )

def sign_in():
    Username = name_entry.get()
    Password = password_entry.get()


    if not all ([Username,Password]):
        messagebox.showwarning("Invaild Input","Please fill all required fields!.")
        return

    try:
        conn = connect_db()
        cur = conn.cursor()

        if cur.execute("SELECT * FROM login WHERE USERNAME=%s AND PASSWORD=%s", (Username, Password)):
            messagebox.showwarning("Invaild Input","Username and Password are already exist.")
            

        elif cur.execute("INSERT INTO sign (USERNAME,PASSWORD) VALUES (%s,%s)",(Username,Password)):
            messagebox.showinfo("Sign Success",f"Welcome, {Username}!")
            conn.commit()
            conn.close()
            root.destroy()
            subprocess.Popen([sys.executable,r"C:\vehicle_project\form ds.py"])

        else:
            messagebox.showerror("Sign Failed","Invaild Username or Password.")
            
    except Exception as e:
        messagebox.showerror("Database error",str(e))
        print("Error during login:",e)



root = tk.Tk()
root.title("Login Page")
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#0f172a")  # dark background

# ---------- Left Frame (Image Section) ----------
left_frame = tk.Frame(root, bg="#0f172a", width=560, height=500)
left_frame.pack(side="left", fill="both")

# Load Image 
img = Image.open(r"C:\Users\Ashik\Downloads\CCAR.jpeg")  
img = img.resize((600, 600))
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(left_frame, image=photo, bg="#0f172a")
img_label.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(left_frame,text="VEHICLE SERVICE MANAGEMENT SYSTEM",font=("Arial", 19, "bold"),fg="dodger blue",bg="gray7").pack(pady=70)

# ---------- Right Frame (Login Section) ----------
right_frame = tk.Frame(root, bg="#020617", width=800, height=500)
right_frame.pack(side="right", fill="both")

# Welcome Text
tk.Label(right_frame,text="WELCOME",font=("Arial", 20, "bold"),fg="dodger blue",bg="#020617").pack(pady=30)

# ---------- Avatar Image ----------
avatar_img = Image.open(r"C:\Users\Ashik\Downloads\avatar.jpeg")
avatar_img = avatar_img.resize((80, 80))
avatar_photo = ImageTk.PhotoImage(avatar_img)

avatar_label = tk.Label(right_frame, image=avatar_photo, bg="#020617")
avatar_label.pack(pady=5)


tk.Label(right_frame,text="SIGN UP",font=("Arial", 15,"bold"),fg="white",bg="#020617").pack(pady=10)

tk.Label(right_frame,text="Create New Username and Password",font=("Arial", 10),fg="gray99",bg="#020617").pack(pady=10)

# ---------- Load Icons ----------
user_icon_img = Image.open(r"C:\Users\Ashik\Downloads\load icon.jpeg").resize((20, 20))
user_icon = ImageTk.PhotoImage(user_icon_img)

lock_icon_img = Image.open(r"C:\Users\Ashik\Downloads\lock.jpeg").resize((20, 20))
lock_icon = ImageTk.PhotoImage(lock_icon_img)

# ---------- Username ----------
tk.Label(right_frame, text="Username", fg="gray", bg="#020617").pack(anchor="w", padx=80)

user_frame = tk.Frame(right_frame, bg="#020617")
user_frame.pack(fill="x", padx=80)

tk.Label(user_frame, image=user_icon, bg="#020617").pack(side="left", padx=(0, 10))

name_entry = tk.Entry(user_frame,font=("Arial", 12),bg="#020617",fg="white",insertbackground="white",bd=0)
name_entry.pack(side="left", fill="x", expand=True)

tk.Frame(right_frame, height=1, bg="gray").pack(fill="x", padx=80, pady=(0, 15))

# ---------- Password ----------
tk.Label(right_frame, text="Password", fg="gray", bg="#020617").pack(anchor="w", padx=80)

pass_frame = tk.Frame(right_frame, bg="#020617")
pass_frame.pack(fill="x", padx=80)

tk.Label(pass_frame, image=lock_icon, bg="#020617").pack(side="left", padx=(0, 10))

password_entry = tk.Entry(pass_frame,font=("Arial", 12),bg="#020617",fg="white",insertbackground="white",bd=0,show="*")
password_entry.pack(side="left", fill="x", expand=True)

tk.Frame(right_frame, height=1, bg="gray").pack(fill="x", padx=80, pady=(0, 20))

# ---------- Login Button ----------
tk.Button(right_frame,text="SIGN UP",font=("Arial", 12, "bold"),bg="#2563eb",fg="white",bd=0,height=2,cursor="hand2",command=sign_in).pack(fill="x", padx=80)

# ---------- Extra Links ----------
tk.Label(right_frame,text="Forgot Password?",fg="gray",bg="#020617",cursor="hand2").pack(pady=10)

tk.Label(right_frame,text="If you have account?  Login Now",fg="#38bdf8",bg="#020617",cursor="hand2").pack()

# ---------- Run App ----------
root.mainloop()


