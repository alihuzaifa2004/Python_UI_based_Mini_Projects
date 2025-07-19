import tkinter as tk
from tkinter import messagebox
import database
import grades
import subprocess
import sys


def launch(username):
    teacher_root = tk.Tk()
    teacher_root.title("Student Dashboard")
    teacher_root.geometry("400x400")
    teacher_root.config(padx=20, pady=20)

    tk.Label(teacher_root, text="Teacher Dashboard", font=("Arial", 18, "bold")).pack(pady=10)


    tk.Label(teacher_root, text=f"Welcome, {username}", font=('Arial', 16)).pack(pady=10)

    def view_classes():
        classes = database.get_all_classes()
        my_classes = [f"{cid} - {info['subject']}" for cid, info in classes.items() if info.get("teacher") == username]
        messagebox.showinfo("My Classes", "\n".join(my_classes) or "No assigned classes.")

    def upload_grades():
        classes = database.get_all_classes()
        my_classes = [cid for cid, info in classes.items() if info.get("teacher") == username]

        def save_grade():
            cid = class_var.get()
            sid = student_var.get()
            mark = entry_marks.get()
            grades.add_grade(sid, cid, mark)
            messagebox.showinfo("Success", f"Grade submitted for {sid}")
            upload_win.destroy()

        upload_win = tk.Toplevel(teacher_root)
        tk.Label(upload_win, text="Class").pack()
        class_var = tk.StringVar(upload_win)
        tk.OptionMenu(upload_win, class_var, *my_classes).pack()

        tk.Label(upload_win, text="Student").pack()
        student_var = tk.StringVar(upload_win)
        class_students = []
        if my_classes:
            class_students = database.get_all_classes()[my_classes[0]].get("students", [])
        tk.OptionMenu(upload_win, student_var, *class_students).pack()

        tk.Label(upload_win, text="Marks").pack()
        entry_marks = tk.Entry(upload_win)
        entry_marks.pack()

        tk.Button(upload_win, text="Submit", command=save_grade).pack()
    def logout():
        teacher_root.destroy()
        subprocess.Popen([sys.executable, "main.py"])


    tk.Button(teacher_root, text="View My Classes", command=view_classes).pack(pady=5)
    tk.Button(teacher_root, text="Upload Grades", command=upload_grades).pack(pady=5)
    tk.Button(teacher_root, text="Logout", command=logout, fg="red").pack(pady=10)

    teacher_root.mainloop()
