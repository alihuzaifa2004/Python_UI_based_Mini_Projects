import tkinter as tk
from tkinter import simpledialog, messagebox
import database
import subprocess
import sys

def launch(username):
    admin_root = tk.Tk()
    admin_root.title("Admin Dashboard")
    admin_root.geometry("350x300")
    admin_root.resizable(True, True)
    label_heading = tk.Label(admin_root, text="Admin Dashboard", font=("Arial", 18, "bold"))
    label_heading.pack(pady=10)
    tk.Label(admin_root, text=f"Welcome, {username}", font=('Arial', 16)).pack(pady=10)
    tk.Label(admin_root, text="Admin Panel", font=('Arial', 16)).pack(pady=10)

    def create_class():
        cid = simpledialog.askstring("Class ID", "Enter Class ID:")
        subject = simpledialog.askstring("Subject", "Enter Subject Name:")
        schedule = simpledialog.askstring("Schedule", "e.g. Mon 10AM:")
        teacher = simpledialog.askstring("Teacher", "Enter Teacher Username:")
        classes = database.get_all_classes()
        classes[cid] = {"subject": subject, "schedule": schedule, "teacher": teacher, "students": []}
        database.save_all_classes(classes)
        messagebox.showinfo("Success", "Class created!")

    def view_all():
        users = database.get_all_users()
        classes = database.get_all_classes()
        msg = f"Users:\n" + "\n".join([f"{u} - {d['role']}" for u, d in users.items()])
        msg += "\n\nClasses:\n" + "\n".join([f"{c}: {info['subject']} by {info['teacher']}" for c, info in classes.items()])
        messagebox.showinfo("Data", msg)

    def logout():
        admin_root.destroy()
        subprocess.Popen([sys.executable, "main.py"])

    tk.Button(admin_root, text="Create New Class", command=create_class).pack(pady=5)
    tk.Button(admin_root, text="View All Data", command=view_all).pack(pady=5)
    tk.Button(admin_root, text="Logout", command=logout, fg="red").pack(pady=10)

    admin_root.mainloop()
