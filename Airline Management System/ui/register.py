import tkinter as tk
from tkinter import messagebox
from core.auth import register_user

def register_screen(root):
    win = tk.Toplevel(root)
    win.title("Register")
    win.geometry("400x300")

    tk.Label(win, text="Register", font=("Arial", 16)).pack(pady=10)
    tk.Label(win, text="Username").pack()
    username_entry = tk.Entry(win)
    username_entry.pack()
    tk.Label(win, text="Password").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()
    tk.Label(win, text="Role").pack()
    role = tk.StringVar(value="customer")
    tk.OptionMenu(win, role, "admin", "employee", "customer").pack()

    def attempt_register():
        file_path = f"data/users/{'staff' if role.get() == 'employee' else role.get()}s.json"
        new_user = {"username": username_entry.get(), "password": password_entry.get(), "role": role.get()}
        if register_user(new_user, file_path):
            messagebox.showinfo("Success", "User registered")
            win.destroy()
        else:
            messagebox.showerror("Error", "Username already exists")

    tk.Button(win, text="Register", command=attempt_register).pack(pady=10)
    