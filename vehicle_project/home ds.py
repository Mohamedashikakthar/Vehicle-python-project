

import tkinter as tk
from tkinter import font,messagebox,ttk
from PIL import Image,ImageTk,ImageFilter
import pymysql
import subprocess
import sys  
import os
root = tk.Tk()
root.title("Login Page")
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#0f172a")  # dark background

def login():
    subprocess.Popen([sys.executable,r"C:\python akil\login ds.py"])

def sign():
    subprocess.Popen([sys.executable,r"C:\python akil\sign ds.py"])


# ---------- Left Frame (Image Section) ----------
left_frame = tk.Frame(root, bg="#0f172a", width=680, height=500)
left_frame.pack(side="left", fill="both")

# Load Image 
img = Image.open(r"C:\Users\Ashik\Downloads\CAR.jpeg")  
img = img.resize((680, 600))
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(left_frame, image=photo, bg="#0f172a")
img_label.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(left_frame,text="VEHICLE SERVICE MANAGEMENT SYSTEM",font=("Arial", 22, "bold"),fg="dodger blue",bg="gray7").pack(pady=70)


# ---------- Right Frame (Login Section) ----------
right_frame = tk.Frame(root, bg="#020617", width=700, height=500)
right_frame.pack(side="right", fill="both")

# Welcome Text
tk.Label(right_frame,text="WELCOME",font=("Arial", 20, "bold"),fg="white",bg="#020617").pack(pady=30)

# ---------- Avatar Image ----------
avatar_img = Image.open(r"C:\Users\Ashik\Downloads\avatar.jpeg")
avatar_img = avatar_img.resize((80, 80))
avatar_photo = ImageTk.PhotoImage(avatar_img)

avatar_label = tk.Label(right_frame, image=avatar_photo, bg="#020617")
avatar_label.pack(pady=5)

tk.Label(right_frame,text=" Create New Username and Password ",font=("Arial", 13),fg="white",bg="#020617").pack(pady=10)

# ---------- Sign Button ----------
tk.Button(right_frame,text="SIGN UP",font=("Arial", 14, "bold"),bg="#2563eb",fg="white",bd=0,height=2,command=sign).pack(fill="x", padx=80)


tk.Label(right_frame,text="OR",font=("Arial", 16,"bold"),fg="white",bg="#020617").pack(pady=10)


tk.Label(right_frame,text="Access Existing Account",font=("Arial", 13),fg="white",bg="#020617").pack(pady=10)

# ---------- login Button ----------
tk.Button(right_frame,text="LOGIN",font=("Arial", 15, "bold"),bg="#2563eb",fg="white",bd=0,height=2,command=login).pack(fill="x", padx=100)




root.mainloop()
#"#1c1c1c"
