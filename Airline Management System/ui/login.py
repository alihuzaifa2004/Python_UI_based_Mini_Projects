import tkinter as tk
from tkinter import messagebox
from core.auth import authenticate_user
from dashboards.admin import admin_dashboard
from dashboards.employee import employee_dashboard
from dashboards.customer import customer_dashboard

def login_screen(root):
    win = tk.Toplevel(root)
    win.title("Login")
    win.geometry("400x300")

    tk.Label(win, text="Login", font=("Arial", 16)).pack(pady=10)

    tk.Label(win, text="Username").pack()
    username_entry = tk.Entry(win)
    username_entry.pack()

    tk.Label(win, text="Password").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    tk.Label(win, text="Role").pack()
    role = tk.StringVar(value="customer")
    tk.OptionMenu(win, role, "admin", "employee", "customer").pack()

    def attempt_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        selected_role = role.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return

        file_path = f"data/users/{'staff' if selected_role == 'employee' else selected_role}s.json"

        if authenticate_user(username, password, file_path):
            messagebox.showinfo("Success", "Login successful!")
            win.destroy()

            if selected_role == "admin":
                admin_dashboard(username)
            elif selected_role == "employee":
                employee_dashboard(username)
            else:
                customer_dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(win, text="Login", command=attempt_login).pack(pady=10)
