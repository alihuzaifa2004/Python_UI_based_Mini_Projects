import tkinter as tk
from tkinter import messagebox
import database
import grades
import schedule
import subprocess
import sys

def launch(username):
    student_root = tk.Tk()
    student_root.title("Student Dashboard")
    student_root.geometry("350x300")
    student_root.resizable(True, True)
    label_heading = tk.Label(student_root, text="Student Dashboard", font=("Arial", 18, "bold"))
    label_heading.pack(pady=10)


    tk.Label(student_root, text=f"Welcome, {username}", font=('Arial', 16)).pack(pady=10)

    def view_schedule():
        classes = database.get_all_classes()
        user_classes = [cid for cid, info in classes.items() if username in info.get("students", [])]
        msg = "\n".join([f"{cid} - {classes[cid]['subject']} on {classes[cid]['schedule']}" for cid in user_classes])
        messagebox.showinfo("My Schedule", msg if msg else "No classes enrolled.")

    def enroll_class():
        classes = database.get_all_classes()
        options = [cid for cid in classes if username not in classes[cid].get("students", [])]

        def enroll():
            selected = class_var.get()
            if selected:
                classes[selected].setdefault("students", []).append(username)
                database.save_all_classes(classes)
                messagebox.showinfo("Enrolled", f"Enrolled in {selected}")
                enroll_win.destroy()

        enroll_win = tk.Toplevel(student_root)
        tk.Label(enroll_win, text="Select class to enroll").pack()
        class_var = tk.StringVar(enroll_win)
        class_menu = tk.OptionMenu(enroll_win, class_var, *options)
        class_menu.pack()
        tk.Button(enroll_win, text="Enroll", command=enroll).pack()

    def view_grades():
        msg = grades.get_student_grades(username)
        messagebox.showinfo("My Grades", msg)

    def logout():
        student_root.destroy()
        subprocess.Popen([sys.executable, "main.py"])

    tk.Button(student_root, text="View Schedule", command=view_schedule).pack(pady=5)
    tk.Button(student_root, text="Enroll in Class", command=enroll_class).pack(pady=5)
    tk.Button(student_root, text="View Grades", command=view_grades).pack(pady=5)
    tk.Button(student_root, text="Logout", command=logout, fg="red").pack(pady=10)

    student_root.mainloop()
