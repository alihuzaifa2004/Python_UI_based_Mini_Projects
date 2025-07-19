import tkinter as tk
from tkinter import ttk, messagebox
import auth
import student
import teacher
import admin

def login_user():
    username = username_entry.get()
    password = password_entry.get()
    selected_role = role_var.get()
    user = auth.login(username, password, selected_role)
    if user:
        messagebox.showinfo("Login Successful", f"Welcome {username}!")
        root.destroy()
        role = user["role"]
        if role == "student":
            student.launch(username)
        elif role == "teacher":
            teacher.launch(username)
        elif role == "admin":
            admin.launch(username)
    else:
        messagebox.showerror("Error", "Invalid credentials or role mismatch.")

def register_user():
    username = username_entry.get()
    password = password_entry.get()
    role = role_var.get()
    success, msg = auth.register(username, password, role)
    if success:
        messagebox.showinfo("Success", msg)
    else:
        messagebox.showerror("Error", msg)

root = tk.Tk()
root.title("🏫School Management System")
root.geometry("400x400")
root.config(padx=20, pady=20)

tk.Label(root, text="🏫School Management System", font=("Arial", 18, "bold")).pack(pady=10)


tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Label(root, text="Role").pack()
role_var = ttk.Combobox(root, values=["student", "teacher", "admin"])
role_var.set("student")
role_var.pack()

tk.Button(root, text="Login", command=login_user).pack(pady=5)
tk.Button(root, text="Register", command=register_user).pack()

root.mainloop()
