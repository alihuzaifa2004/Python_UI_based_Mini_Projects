import tkinter as tk
from tkinter import messagebox
from core.flight_ops import load_flights, add_flight, remove_flight

def admin_dashboard(username):
    win = tk.Toplevel()
    win.title("Admin Dashboard")
    win.geometry("600x400")
    tk.Label(win, text=f"Welcome Admin {username}", font=("Arial", 16)).pack(pady=10)

    def view_flights():
        flights = load_flights()
        valid_flights = [
            f for f in flights
            if isinstance(f, dict) and all(k in f for k in ("id", "origin", "destination"))
        ]
        if not valid_flights:
            messagebox.showinfo("All Flights", "No valid flights found.")
            return
        msg = "\n".join([f"{f['id']} | {f['origin']} -> {f['destination']}" for f in valid_flights])
        messagebox.showinfo("All Flights", msg)

    def add_flight_ui():
        add_win = tk.Toplevel(win)
        add_win.title("Add Flight")
        tk.Label(add_win, text="Flight ID").pack()
        flight_id = tk.Entry(add_win)
        flight_id.pack()
        tk.Label(add_win, text="Origin").pack()
        origin = tk.Entry(add_win)
        origin.pack()
        tk.Label(add_win, text="Destination").pack()
        dest = tk.Entry(add_win)
        dest.pack()

        def submit():
            new_flight = {"id": flight_id.get(), "origin": origin.get(), "destination": dest.get()}
            add_flight(new_flight)
            messagebox.showinfo("Success", "Flight added")
            add_win.destroy()

        tk.Button(add_win, text="Submit", command=submit).pack(pady=10)

    tk.Button(win, text="View Flights", command=view_flights).pack(pady=5)
    tk.Button(win, text="Add Flight", command=add_flight_ui).pack(pady=5)
