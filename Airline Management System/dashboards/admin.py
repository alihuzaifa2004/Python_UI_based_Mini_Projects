import tkinter as tk
from tkinter import messagebox
from core.flight_ops import load_flights, add_flight, remove_flight

def admin_dashboard(username, logout_callback):
    win = tk.Toplevel()
    win.title("Admin Dashboard")
    tk.Label(win, text="Admin Portal", font=("Arial", 16)).pack(pady=10)
    win.geometry("300x400")
    win.protocol("WM_DELETE_WINDOW", lambda: (logout_callback(), win.destroy()))

    tk.Label(win, text=f"Welcome Admin {username}", font=("Arial", 16)).pack(pady=10)

    def view_flights():
        flights = load_flights()
        valid_flights = [
            f for f in flights
            if isinstance(f, dict) and all(k in f for k in ("id", "origin", "destination", "time"))
        ]
        if not valid_flights:
            messagebox.showinfo("All Flights", "No valid flights found.")
            return
        msg = "\n".join([
            f"{f['id']} | {f['origin']} -> {f['destination']} | {f.get('date', 'N/A')} {f.get('time', '')}"
            for f in valid_flights])
        
        messagebox.showinfo("All Flights", msg)
        
    def add_flight_ui():
        add_win = tk.Toplevel(win)
        add_win.title("Add Flight")
        tk.Label(add_win, text="Add Flight", font=("Arial", 16)).pack(pady=10)
    
        add_win.geometry("300x400")

        tk.Label(add_win, text="Flight ID").pack()
        flight_id = tk.Entry(add_win)
        flight_id.pack()

        tk.Label(add_win, text="Origin").pack()
        origin = tk.Entry(add_win)
        origin.pack()

        tk.Label(add_win, text="Destination").pack()
        dest = tk.Entry(add_win)
        dest.pack()

        tk.Label(add_win, text="Date (YYYY-MM-DD)").pack()
        date = tk.Entry(add_win)
        date.pack()

        tk.Label(add_win, text="Time (HH:MM)").pack()
        time = tk.Entry(add_win)
        time.pack()

        def submit():
            from datetime import datetime
            from core.flight_ops import load_flights, add_flight

            new_id = flight_id.get().strip()
            new_origin = origin.get().strip()
            new_dest = dest.get().strip()
            new_date = date.get().strip()
            new_time = time.get().strip()

            # ✅ Check that all fields are filled
            if not all([new_id, new_origin, new_dest, new_date, new_time]):
                messagebox.showerror("Error", "All fields are required.")
                return

            # ✅ Validate date and time format
            try:
                datetime.strptime(new_date, "%Y-%m-%d")
                datetime.strptime(new_time, "%H:%M")
            except ValueError:
                messagebox.showerror("Error", "Invalid date or time format.")
                return

            # ✅ Check if flight ID already exists
            flights = load_flights()
            if any(f.get("id") == new_id for f in flights):
                messagebox.showerror("Error", f"Flight ID '{new_id}' already exists.")
                return

            new_flight = {
                "id": new_id,
                "origin": new_origin,
                "destination": new_dest,
                "date": new_date,
                "time": new_time
            }

            add_flight(new_flight)
            messagebox.showinfo("Success", "Flight added successfully.")
            add_win.destroy()

        tk.Button(add_win, text="Submit", command=submit).pack(pady=10)


    def logout():
        logout_callback()
        win.destroy()

    # Dashboard buttons
    tk.Button(win, text="View Flights", command=view_flights).pack(pady=5)
    tk.Button(win, text="Add Flight", command=add_flight_ui).pack(pady=5)
    tk.Button(win, text="Logout", command=logout, fg="white", bg="red").pack(pady=10)
