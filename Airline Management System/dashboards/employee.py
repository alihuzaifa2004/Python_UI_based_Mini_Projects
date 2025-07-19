import tkinter as tk
from tkinter import messagebox

def employee_dashboard(username):
    win = tk.Toplevel()
    win.title("Employee Dashboard")
    win.geometry("400x300")
    tk.Label(win, text=f"Welcome Employee {username}", font=("Arial", 16)).pack(pady=10)

    tk.Label(win, text="Feature: View assigned flights [Coming Soon]").pack(pady=10)
