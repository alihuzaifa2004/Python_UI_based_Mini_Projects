import tkinter as tk
from tkinter import messagebox
from core.auth import authenticate_user, register_user
from dashboards.admin import admin_dashboard
from dashboards.employee import employee_dashboard
from dashboards.customer import customer_dashboard

# Global root for reuse
app_root = tk.Tk()


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_login(frame):
    clear_frame(frame)
    tk.Label(frame, text="🛫Airline Management System", font=("Arial", 16)).pack(pady=10)
    tk.Label(frame, text="Username").pack()
    username = tk.Entry(frame)
    username.pack()
    tk.Label(frame, text="Password").pack()
    password = tk.Entry(frame, show="*")
    password.pack()
    tk.Label(frame, text="Role").pack()
    role = tk.StringVar(value="customer")
    tk.OptionMenu(frame, role, "admin", "employee", "customer").pack()

    def do_login():
        user = username.get().strip()
        pwd = password.get().strip()
        r = role.get()
        path = f"data/users/{'staff' if r=='employee' else r}s.json"
        if authenticate_user(user, pwd, path):
            messagebox.showinfo("Success", "Login successful!")
            app_root.withdraw()  # hide main window
            if r == "admin":
                admin_dashboard(user, logout_callback=lambda: show_login_frame())
            elif r == "employee":
                employee_dashboard(user, logout_callback=lambda: show_login_frame())
            else:
                customer_dashboard(user, logout_callback=lambda: show_login_frame())
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(frame, text="Login", command=do_login).pack(pady=10)
    tk.Button(frame, text="No account? Register", command=lambda: show_register(frame)).pack()

def show_register(frame):
    clear_frame(frame)
    tk.Label(frame, text="Register", font=("Arial", 16)).pack(pady=10)
    tk.Label(frame, text="Username").pack()
    username = tk.Entry(frame)
    username.pack()
    tk.Label(frame, text="Password").pack()
    password = tk.Entry(frame, show="*")
    password.pack()
    tk.Label(frame, text="Role").pack()
    role = tk.StringVar(value="customer")
    tk.OptionMenu(frame, role, "admin", "employee", "customer").pack()

    def do_register():
        user = username.get().strip()
        pwd = password.get().strip()
        r = role.get()
        path = f"data/users/{'staff' if r=='employee' else r}s.json"
        if register_user({"username": user, "password": pwd, "role": r}, path):
            messagebox.showinfo("Success", "Registered! You can login now.")
            show_login(frame)
        else:
            messagebox.showerror("Error", "User already exists")

    tk.Button(frame, text="Register", command=do_register).pack(pady=10)
    tk.Button(frame, text="Back to Login", command=lambda: show_login(frame)).pack()

def show_login_frame():
    app_root.deiconify()
    show_login(wrapper)

app_root.title("Airline Management System")
app_root.geometry("400x350")
wrapper = tk.Frame(app_root)
wrapper.pack(expand=True)
show_login(wrapper)
app_root.mainloop()
