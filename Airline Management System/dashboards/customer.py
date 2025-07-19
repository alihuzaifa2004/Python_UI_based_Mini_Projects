import tkinter as tk
from tkinter import messagebox
from core.flight_ops import load_flights

def customer_dashboard(username):
    win = tk.Toplevel()
    win.title("Customer Dashboard")
    win.geometry("400x300")
    tk.Label(win, text=f"Welcome {username}", font=("Arial", 16)).pack(pady=10)

    def view_flights():
        flights = load_flights()
        valid_flights = [
            f for f in flights
            if isinstance(f, dict) and all(k in f for k in ("id", "origin", "destination"))
        ]
        if not valid_flights:
            messagebox.showinfo("Available Flights", "No valid flights available.")
            return

        msg = "\n".join([f"{f['id']}: {f['origin']} -> {f['destination']}" for f in valid_flights])
        messagebox.showinfo("Available Flights", msg)

    tk.Button(win, text="View Flights", command=view_flights).pack(pady=10)
